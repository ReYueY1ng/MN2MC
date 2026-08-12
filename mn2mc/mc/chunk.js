const { performance } = require('perf_hooks')
const zlib = require('zlib')
const fs = require('fs/promises')
const BitArray = require('prismarine-chunk/src/pc/common/BitArrayNoSpan')

const MAX_PARSED_CACHE = 100

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Monkey-patch prismarine-chunk's loadParsedLight.
 *
 * Upstream bug: the vanilla server serializes each light section as the
 * DataLayer's flat nibble byte array (byte = pos>>1, low nibble for even pos,
 * high nibble for odd pos; pos = (y<<8)|(z<<4)|x) — see
 * ClientboundLightUpdatePacketData.DATA_LAYER_STREAM_CODEC = byteArray(2048).
 * But the stock loadParsedLight feeds those bytes into BitArray.readBuffer(),
 * which expects Mojang's packed-64-bit-long layout (big-endian u32 pairs, the
 * format used by block palette data). The mismatch mirrors the x-axis within
 * every 16-block row: value read at (x,y,z) is actually the light of
 * (14-x+2*(x&1), y, z).
 *
 * Fix: build the BitArray straight from the raw nibble bytes (same approach as
 * the upstream _loadBlockLightNibbles), bypassing readBuffer entirely.
 */
function patchLoadParsedLight(ChunkClass) {
    if (ChunkClass.prototype._mn2mcLightPatched) return
    Object.defineProperty(ChunkClass.prototype, '_mn2mcLightPatched', { value: true, configurable: true })
    ChunkClass.prototype.loadParsedLight = function (skyLight, blockLight, skyLightMask, blockLightMask, emptySkyLightMask, emptyBlockLightMask) {
        function readSection(sections, data, lightMask, pLightMask, emptyMask, pEmptyMask) {
            let currentSectionIndex = 0
            const incomingLightMask = BitArray.fromLongArray(pLightMask, 1)
            const incomingEmptyMask = BitArray.fromLongArray(pEmptyMask, 1)
            for (let y = 0; y < sections.length; y++) {
                const isEmpty = incomingEmptyMask.get(y)
                if (!incomingLightMask.get(y) && !isEmpty) continue
                emptyMask.set(y, isEmpty)
                lightMask.set(y, 1 - isEmpty)
                if (!isEmpty) {
                    const raw = data[currentSectionIndex++]
                    if (raw.length !== 2048) throw new Error('Invalid light nibble buffer length ' + raw.length)
                    sections[y] = new BitArray({
                        bitsPerValue: 4,
                        capacity: 4096,
                        data: new Int8Array(raw).buffer
                    })
                } else {
                    sections[y] = new BitArray({ bitsPerValue: 4, capacity: 4096 })
                }
            }
        }
        readSection(this.skyLightSections, skyLight, this.skyLightMask, skyLightMask, this.emptySkyLightMask, emptySkyLightMask)
        readSection(this.blockLightSections, blockLight, this.blockLightMask, blockLightMask, this.emptyBlockLightMask, emptyBlockLightMask)
    }
}

class ChunkManager {
    constructor(version, pyclient, mcclient, registry, transportMode, channelName, bufferSize) {
        this.version = version
        this.pyclient = pyclient
        this.registry = registry
        this.mcclient = mcclient
        this.minY = -64
        this.worldHeight = 384
        //this.minY = 0
        //this.worldHeight = 256
        this.chunk = new prismarineChunk(this.version)
        patchLoadParsedLight(this.chunk)
        this.cacheChunks = []
        this.cacheParsedChunks = []
        this.running = true
        this.transportReady = false
        this.transportMode = transportMode || 'legacy'
        this.transportPort = null
        this._tcpSocket = null
        this._tcpServer = null
        this._writer = null
        this.mcclient.on("registry_data", (data) => {
            if (data.id == "minecraft:dimension_type") {
                this.registry.loadDimensionCodec(data)
            }
        })
        let setDimension = (packet) => {
            if (!this.registry.dimensionsById) return
            let data = this.registry.dimensionsById[packet.worldState.dimension]
            if (!data) return
            this.minY = data.minY
            this.worldHeight = data.height
        }
        this.mcclient.on('login', setDimension)
        this.mcclient.on('respawn', setDimension)
        this.mcclient.on('map_chunk', (jsondata) => this.cacheChunks.push(jsondata))
        // Forward update_light to Python with sec_y already resolved (this
        // class owns minY, which Python cannot see). mask bits = light section
        // indexes; sec_y = idx - 1 + minY/16 (getLightSectionIndex inverse).
        this.mcclient.on('update_light', (jsondata) => {
            const offset = this.minY / 16
            const remap = (mask) => (mask || []).map(n => {
                const v = typeof n === 'bigint' ? n : BigInt(n)
                const bits = []
                for (let i = 0; i < 64; i++) {
                    if (v & (1n << BigInt(i))) bits.push(i - 1 + offset)
                }
                return bits
            }).flat()
            jsondata._secY = {
                sky: remap(jsondata.skyLightMask),
                block: remap(jsondata.blockLightMask)
            }
            this.pyclient.on_packet(jsondata, { name: 'update_light' })
        })
        //this.intervalId = setInterval(async () => this.pushPyEvent(), 200)
        this._initTransport(channelName, bufferSize)
        return
    }

    _initTransport(channelName, bufferSize) {
        if (this.transportMode === 'kren') {
            try {
                const kren = require('@pawanxz/kren')
                this._writer = new kren.Writer(channelName, bufferSize)
                this.transportReady = true
            } catch (err) {
                console.error(`KREN transport init failed: ${err.message}`)
                this.transportReady = true // allow parseChunks to run, data will be lost
            }
        } else if (this.transportMode === 'tcp') {
            const net = require('net')
            this._tcpServer = net.createServer((socket) => {
                socket.setNoDelay(true)
                this._tcpSocket = socket
            })
            this._tcpServer.listen(0, '127.0.0.1', () => {
                this.transportPort = this._tcpServer.address().port
                this.transportReady = true
            })
        } else {
            // legacy mode: no special transport, use compressedChunks getter
            this.transportReady = true
        }
        // Start parseChunks after transport is set up
        this.parseChunks()
    }

    async parseChunks() {
        let processedChunks = 0
        while (this.running) {
            if (!this.transportReady) {
                await sleep(10)
                continue
            }
            let jsondata = this.cacheChunks.shift()
            if (jsondata == undefined) {
                await sleep(200)
                continue
            } else if (processedChunks >= 10) {
                await sleep(250)
                processedChunks = 0
            }
            processedChunks++
            await this.onEvent(jsondata)
        }
        
        this.stop()
    }

    async onEvent(jsondata) {
        let isLoaded = false
        try {
            var chunk = new this.chunk({
                minY: this.minY,
                worldHeight: this.worldHeight
            })
            chunk.load(jsondata.chunkData)
            isLoaded = true
        } catch (error) {
            console.warn(`Failed to decode chunk data (${jsondata.x}, ${jsondata.y}), fallback to old options: ${error}`)
            if (this.worldHeight == 256) {
                var dimdatas = [[-64, 384]]
            } else if (this.worldHeight == 384) {
                var dimdatas = [[0, 256]]
            } else {
                var dimdatas = [[0, 256], [-64, 384]]
            }
            for (var data of dimdatas) {
                try {
                    var chunk = new this.chunk({
                        minY: data[0],
                        worldHeight: data[1]
                    })
                    chunk.load(jsondata.chunkData)
                    isLoaded = true
                    break
                } catch (error) {
                    continue
                }
            }
        }
        if (!isLoaded) {
            console.error(`Failed to decode chunk data (${jsondata.x}, ${jsondata.z})`)
            return
        }
        // Light arrives as top-level packet fields (minecraft-protocol parses
        // skyLight/blockLight as per-section u8 arrays + masks). prismarine-
        // chunk does NOT parse them from chunkData, so load them explicitly
        // or skyLightSections stays all-null (no light reaches the client).
        // The masks are varint longs (plain numbers); prismarine-chunk's
        // fromLongArray expects [high, low] pairs, so convert before passing.
        if (jsondata.skyLight || jsondata.blockLight) {
            chunk.loadParsedLight(
                jsondata.skyLight, jsondata.blockLight,
                this._toLongArray(jsondata.skyLightMask),
                this._toLongArray(jsondata.blockLightMask),
                this._toLongArray(jsondata.emptySkyLightMask),
                this._toLongArray(jsondata.emptyBlockLightMask)
            )
        }
        if (this.cacheParsedChunks.length >= MAX_PARSED_CACHE) return
        let blocks = []
        const sections = chunk.sections
        const hasSectionAPI = Array.isArray(sections)
        for (let y = 0; y < 256; y++) {
            if (hasSectionAPI) {
                const sectionIdx = Math.floor((y - this.minY) / 16)
                const section = sections[sectionIdx]
                if (section && typeof section.blockCount === 'number' && section.blockCount === 0) {
                    y += 15  // skip remaining rows in this empty section
                    continue
                }
            }
            for (let x = 0; x < 16; x++) {
                for (let z = 0; z < 16; z++) {
                    let block = chunk.getBlock(Vec3(x, y, z))
                    let type = block.type
                    let properties = block.getProperties()
                    if (type != 0) {
                        if (Object.keys(properties).length === 0) {
                            blocks.push([x, y, z, type])
                        } else {
                            blocks.push([x, y, z, type, properties])
                        }
                    }
                }
            }
        }
        const lights = this.extractLights(chunk)
        this.cacheParsedChunks.push({ x: jsondata.x, z: jsondata.z, blocks: blocks, lights: lights })

        // Non-legacy transports: send immediately after each chunk is parsed
        if (this.transportMode === 'kren' && this._writer) {
            this._flushKren()
        } else if (this.transportMode === 'tcp' && this._tcpSocket) {
            this._flushTcp()
        }
    }

    /**
     * Extract per-section sky/block light nibble arrays for Mini World.
     *
     * Mini World section light = 4 layers of u8[2048] (4096 nibbles, one per
     * block in linear = lx + lz*16 + ly*256 layout). prismarine-chunk stores
     * light in skyLightSections/blockLightSections indexed by
     * getLightSectionIndex(pos) = floor((pos.y - minY) / 16) + 1, and its
     * linear index is ((y & 15) << 8) | (z << 4) | x — the SAME layout Mini
     * World uses. So we read nibbles in linear order and re-pack them into
     * 2048-byte arrays (2 nibbles per byte, low nibble = even index).
     *
     * @param {object} chunk prismarine-chunk ChunkColumn
     * @returns {Array<{sec_y: number, sky: Uint8Array, block: Uint8Array}>}
     */
    extractLights(chunk) {
        const lights = []
        for (let secY = 0; secY < 16; secY++) {
            const worldY = secY * 16
            const li = Math.floor((worldY - this.minY) / 16) + 1
            const skySec = chunk.skyLightSections[li]
            const blockSec = chunk.blockLightSections[li]
            if (!skySec && !blockSec) continue
            const light = { sec_y: secY }
            if (skySec) light.sky = this._packNibbles(skySec)
            if (blockSec) light.block = this._packNibbles(blockSec)
            lights.push(light)
        }
        return lights
    }

    _packNibbles(bitArray) {
        // Re-pack 4096 nibbles into Mini World linear layout (lx + lz*16 +
        // ly*256). prismarine-chunk's light BitArray uses the same linear
        // index (MC getSectionBlockIndex = ((ly<<8)|(lz<<4)|lx)), so the
        // values map 1:1 with no axis transform (verified in-game: block
        // placement flips x in send_fast_chunk, light does NOT).
        const out = new Uint8Array(2048)
        for (let i = 0; i < 2048; i++) {
            out[i] = bitArray.get(i * 2) | (bitArray.get(i * 2 + 1) << 4)
        }
        return out
    }

    _toLongArray(mask) {
        if (!mask) return []
        return mask.map(n => {
            const v = typeof n === 'bigint' ? n : BigInt(n)
            return [Number(v >> 32n), Number(v & 0xFFFFFFFFn)]
        })
    }

    _flushKren() {
        if (this.cacheParsedChunks.length === 0) return
        try {
            const compressed = zlib.deflateSync(msgpackr.pack(this.cacheParsedChunks))
            this._writer.write(compressed)
        } catch (err) {
            console.error(`KREN write error: ${err.message}`)
        }
        this.cacheParsedChunks.length = 0
    }

    _flushTcp() {
        if (this.cacheParsedChunks.length === 0) return
        try {
            const compressed = zlib.deflateSync(msgpackr.pack(this.cacheParsedChunks))
            const header = Buffer.alloc(4)
            header.writeUInt32BE(compressed.length, 0)
            this._tcpSocket.write(Buffer.concat([header, compressed]))
        } catch (err) {
            console.error(`TCP send error: ${err.message}`)
        }
        this.cacheParsedChunks.length = 0
    }

    stop() {
        this.running = false
        if (this._tcpSocket) {
            try { this._tcpSocket.destroy() } catch (_) {}
            this._tcpSocket = null
        }
        if (this._tcpServer) {
            try { this._tcpServer.close() } catch (_) {}
            this._tcpServer = null
        }
        // kren Writer: set to null, GC will trigger shm_unlink
        if (this.transportMode === 'kren') {
            const name = this._writer.name
            const path = '/dev/shm/kren_' + name
            this._writer = null
            // 在部分情况下（比如关闭代理）不会清理共享内存，这里手动清理一下
            fs.rm(path, {force: true})
            .catch((reason) => {
                console.error(`Failed to remove kren shm file ${name}: ${reason}`)
            })
        }
    }

    async pushPyEvent() {
        if (this.running) {
            if (this.cacheParsedChunks.length > 0) {
                console.log('send')
                const ms = performance.now()
                await this.pyclient.on_packet(this.cacheParsedChunks, { name: 'parsed_chunk' })
                this.cacheParsedChunks = []
                console.log('sent ' + (performance.now() - ms) + ' ms')
            }
        } else {
            clearInterval(this.intervalId)
        }
    }

    get compressedChunks() {
        let compressed = zlib.deflateSync(msgpackr.pack(this.cacheParsedChunks))
        this.cacheParsedChunks.length = 0
        return compressed
    }
}

module.exports = ChunkManager

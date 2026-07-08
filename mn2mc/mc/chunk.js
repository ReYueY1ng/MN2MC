const { performance } = require('perf_hooks')
const zlib = require('zlib')

const MAX_PARSED_CACHE = 100

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
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
        //console.log('Parse done')
        this.cacheParsedChunks.push({ x: jsondata.x, z: jsondata.z, blocks: blocks })

        // Non-legacy transports: send immediately after each chunk is parsed
        if (this.transportMode === 'kren' && this._writer) {
            this._flushKren()
        } else if (this.transportMode === 'tcp' && this._tcpSocket) {
            this._flushTcp()
        }
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
        // kren Writer: no explicit close needed, GC handles cleanup
        this._writer = null
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

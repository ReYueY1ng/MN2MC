const { performance } = require('perf_hooks')
const zlib = require('zlib')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

class ChunkManager {
    constructor(version, pyclient, mcclient, registry) {
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
        this.mcclient.on("registry_data", (data) => {
            if (data.id == "minecraft:dimension_type") {
                this.registry.loadDimensionCodec(data)
            }
        })
        let setDimension = (packet) => {
            let data = this.registry.dimensionsById[packet.worldState.dimension]
            this.minY = data.minY
            this.worldHeight = data.height
        }
        this.mcclient.on('login', setDimension)
        this.mcclient.on('respawn', setDimension)
        this.mcclient.on('map_chunk', (jsondata) => this.cacheChunks.push(jsondata))
        //this.intervalId = setInterval(async () => this.pushPyEvent(), 200)
        this.parseChunks()
        return
    }

    async parseChunks() {
        let processedChunks = 0
        while (this.running) {
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
        let blocks = []
        for (let y = 0; y < 256; y++) {
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
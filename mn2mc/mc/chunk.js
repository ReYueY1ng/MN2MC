const { performance } = require('perf_hooks')
const zlib = require('zlib')

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

class ChunkManager {
    constructor(version, pyclient, mcclient) {
        this.version = version
        this.pyclient = pyclient
        this.mcclient = mcclient
        this.minY = -64
        this.worldHeight = 384
        //this.minY = 0
        //this.worldHeight = 256
        this.chunk = new prismarineChunk(this.version)
        this.cacheChunks = []
        this.cacheParsedChunks = []
        this.running = true
        this.mcclient.on('map_chunk', (jsondata) => this.cacheChunks.push(jsondata))
        //this.intervalId = setInterval(async () => this.pushPyEvent(), 200)
        this.parseChunks()
        return
    }

    async parseChunks() {
        let processedChunks = 0
        while (true) {
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
        let chunk = new this.chunk({
            minY: this.minY,
            worldHeight: this.worldHeight
        })
        chunk.load(jsondata.chunkData)
        let blocks = []
        for (let y = 0; y < 256; y++) {
            for (let x = 0; x < 16; x++) {
                for (let z = 0; z < 16; z++) {
                    let type = chunk.getBlock(Vec3(x, y, z)).type
                    if (type != 0) {
                        blocks.push([x, y, z, type])
                    }
                }
            }
        }
        //console.log('Parse done')
        this.cacheParsedChunks.push({x: jsondata.x, z: jsondata.z, blocks: blocks})
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
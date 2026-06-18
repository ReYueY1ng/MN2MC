from __future__ import annotations

import json
import queue

import javascript
from javascript import require

import mn2mc.config as config
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents.chunk.chunk_parser import (
    create_worker_threads,
    send_air_chunk,
    send_block_updates,
)

prismarine_chunk = require("prismarine-chunk")(config.mc["version"])
Vec3 = require("vec3")
chunkqueue = queue.Queue()
miny: int = -64
worldheight: int = 384

javascript.eval_js("""
    global.Vec3 = Vec3
    global.prismarine_chunk = prismarine_chunk
""")

parse_js = javascript.eval_js("""
    return function(datalist, miny, worldheight) {
        let isLoaded = false
        try {
            var chunk = new prismarine_chunk({
                minY: miny,
                worldHeight: worldheight
            })
            chunk.load(Buffer.from(datalist))
            isLoaded = true
        } catch (error) {
            console.warn(`Failed to decode chunk data, fallback to old options: ${error}`)
            if (worldheight == 256) {
                var dimdatas = [[-64, 384]]
            } else if (worldheight == 384) {
                var dimdatas = [[0, 256]]
            } else {
                var dimdatas = [[0, 256], [-64, 384]]
            }
            for (var data of dimdatas) {
                try {
                    var chunk = new prismarine_chunk({
                        minY: data[0],
                        worldHeight: data[1]
                    })
                    chunk.load(Buffer.from(datalist))
                    isLoaded = true
                    break
                } catch (error) {
                    continue
                }
            }
        }
        if (!isLoaded) {
            console.error(`Failed to decode chunk data`)
            return JSON.stringify([])
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
        return JSON.stringify(blocks)
    }
""")


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    chunkqueue.put((client, jsondata))


def parse_new(client: MCClient, jsondata: dict):
    cx = -jsondata["x"] - 1
    cz = jsondata["z"]
    send_air_chunk(client.miniplayer, cx, cz)
    output_json = parse_js(jsondata["chunkData"]["data"], miny, worldheight)
    pyblocks = json.loads(output_json)
    send_block_updates(client.miniplayer, cx, cz, pyblocks, flush_threshold=2048)


def stop():
    chunkqueue.shutdown()


def _process(data):
    parse_new(data[0], data[1])


create_worker_threads(_process, chunkqueue)

add_event("map_chunk", on_recv)

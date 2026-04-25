import json
import threading
import queue
import javascript
import mn2mc
from javascript import require

import mn2mc.config as config
import mn2mc.utils.mini_block as mini_block
import mn2mc.mapping.blocks as block_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode, PB_ChunkSaveDB, PB_ChunkBlob
from mn2mc.mini.proto.hc import PB_SyncChunkDataHC, PB_BlockUpdateHC

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
                    let type = chunk.getBlock(Vec3(x, y, z)).type
                    if (type != 0) {
                        blocks.push([x, y, z, type])
                    }
                }
            }
        }
        return JSON.stringify(blocks)
    }
""")
with open("mn2mc/mini/airchunk", "rb") as f:
    air = f.read()


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    chunkqueue.put((client, jsondata))


def parse_new(client: MCClient, jsondata: dict):
    minichunk = PB_SyncChunkDataHC(
        SectionFlags=65535,
        Initialize=1,
        ChunkData=PB_ChunkSaveDB(
            OWID=10239475674329,
            MapID=0,
            x=-jsondata["x"] - 1,
            z=jsondata["z"],
            ChunkBlob=PB_ChunkBlob(UnzipLen=805308264, BlobLen=554, BlobDetail=air),
        ),
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_SYNC_CHUNK_DATA_HC, minichunk)
    # time.sleep(0.1)
    output_json = parse_js(jsondata["chunkData"]["data"], miny, worldheight)
    pyblocks = json.loads(output_json)
    # logger.debug(pyblocks)
    converted_blocks = []
    blocksex = []
    for block in pyblocks:
        if block[3] != 0:
            encoded, quotient = mini_block.encode_block(
                block_mapping.mc_to_mini(block[3]), 15 - block[0], block[1], block[2]
            )
            converted_blocks.append(encoded)
            blocksex.append(quotient)
            if len(blocksex) % 2048 == 0:
                send_blocks(
                    client,
                    -jsondata["x"] - 1,
                    jsondata["z"],
                    converted_blocks,
                    blocksex,
                )
                converted_blocks.clear()
                blocksex.clear()

    send_blocks(client, -jsondata["x"] - 1, jsondata["z"], converted_blocks, blocksex)
    del converted_blocks
    del blocksex


def send_blocks(
    client: MCClient, x: int, z: int, converted_blocks: list, blocksex: list
):
    client.miniplayer.send_packet(
        ePBMsgCode.PB_BLOCK_DATA_UPDATE_HC,
        PB_BlockUpdateHC(
            ChunkX=x,
            ChunkZ=z,
            MapID=0,
            Blocks=converted_blocks,
            BlocksEx=blocksex,
            BlockStateIndex=[0 for _ in range(len(blocksex))],
        ).SerializeToString(),
    )


def chunk_parse_thread():
    while mn2mc.running:
        try:
            data = chunkqueue.get()
            parse_new(data[0], data[1])
        except queue.ShutDown:
            return


def stop():
    chunkqueue.shutdown()


for i in range(config.mc["chunk_parse_thread"]):
    threading.Thread(target=chunk_parse_thread, name=f"Chunk parser {i}").start()

add_event("map_chunk", on_recv)

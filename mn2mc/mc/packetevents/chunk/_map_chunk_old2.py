import json
import threading
import queue
import javascript
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
lock = threading.Lock()

javascript.eval_js("""
    global.Vec3 = Vec3
    global.prismarine_chunk = prismarine_chunk
""")

parse_js = javascript.eval_js("""
    return function(datalist) {
        let chunk = new prismarine_chunk({
        })
        chunk.load(Buffer.from(datalist))
        let blocks = []
        for (let y = 0; y < 256; y++) {
            for (let x = 0; x < 16; x++) {
                for (let z = 0; z < 16; z++) {
                    blocks.push([x, y, z, chunk.getBlock(Vec3(x, y, z)).type])
                }
            }
        }
        return JSON.stringify(blocks)
    }
""")
with open("air", "rb") as f:
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
    output_json = parse_js(jsondata["chunkData"]["data"])
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
    while True:
        lock.acquire()
        data = chunkqueue.get()
        lock.release()
        parse_new(data[0], data[1])


for i in range(config.mc["chunk_parse_thread"]):
    threading.Thread(target=chunk_parse_thread, name=f"Chunk parser {i}").start()

add_event("map_chunk", on_recv)

import json
import threading
import queue
from aiorak import Reliability, Priority
import javascript

import mn2mc.config as config
import mn2mc.utils.mini_block as mini_block
import mn2mc.mapping.blocks as block_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode, PB_ChunkSaveDB, PB_ChunkBlob
from mn2mc.mini.proto.hc import PB_SyncChunkDataHC, PB_BlockUpdateHC
from mn2mc.mini.player import players, MiniPlayer

prismarine_chunk = javascript.require("prismarine-chunk")(config.mc["version"])
Vec3 = javascript.require("vec3")
chunkqueue = queue.Queue()
lock = threading.Lock()

javascript.eval_js("""
    global.Vec3 = Vec3
    global.prismarine_chunk = prismarine_chunk
""")

parse_js = javascript.eval_js("""
    return async function(uin, x, z, datalist) {
        let chunk = new prismarine_chunk({
            minY: 0,
            worldHeight: 256
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
        console.log('Parse done')
        await chunkqueue.put([uin, x, z, JSON.stringify(blocks)])
        console.log('Put done')
    }
""")
with open("air", "rb") as f:
    air = f.read()


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    threading.Thread(target=parse_new, args=(client, jsondata)).start()


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
    parse_js(
        client.miniplayer.uin,
        jsondata["x"],
        jsondata["z"],
        jsondata["chunkData"]["data"],
    )


def parse_done(uin: int, x: int, z: int, output_json: str):
    for player in players:
        if player.uin == uin:
            miniplayer = player
            break
    else:
        return
    pyblocks = json.loads(output_json)
    converted_blocks = []
    blocksex = []
    for block in pyblocks:
        if block[3] != 0:
            encoded, quotient = mini_block.encode_block(
                block_mapping.mc_to_mini(block[3]), 15 - block[0], block[1], block[2]
            )
            converted_blocks.append(encoded)
            blocksex.append(quotient)
            if len(blocksex) % 6000 == 0:
                send_blocks(miniplayer, -x - 1, z, converted_blocks, blocksex)
                converted_blocks.clear()
                blocksex.clear()

    send_blocks(miniplayer, -x - 1, z, converted_blocks, blocksex)
    del converted_blocks
    del blocksex


def send_blocks(
    miniplayer: MiniPlayer, x: int, z: int, converted_blocks: list, blocksex: list
):
    miniplayer.send_packet(
        ePBMsgCode.PB_BLOCK_DATA_UPDATE_HC,
        PB_BlockUpdateHC(
            ChunkX=x,
            ChunkZ=z,
            MapID=0,
            Blocks=converted_blocks,
            BlocksEx=blocksex,
            BlockStateIndex=[0 for _ in range(len(blocksex))],
        ).SerializeToString(),
        Reliability.UNRELIABLE,
        Priority.IMMEDIATE,
    )


def chunk_parse_thread():
    while True:
        lock.acquire()
        data = chunkqueue.get()
        lock.release()
        parse_done(data[0], data[1], data[2], data[3])


for i in range(config.mc["chunk_parse_thread"]):
    threading.Thread(target=chunk_parse_thread, name=f"Chunk parser {i}").start()

add_event("map_chunk", on_recv)

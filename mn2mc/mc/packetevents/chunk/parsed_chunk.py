import queue
import threading

import mn2mc
import mn2mc.config as config
import mn2mc.mapping.block_face as block_face_mapping
import mn2mc.mapping.blocks as block_mapping
import mn2mc.utils.mini_block as mini_block
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.proto.common import PB_ChunkBlob, PB_ChunkSaveDB, ePBMsgCode
from mn2mc.mini.proto.hc import PB_BlockUpdateHC, PB_SyncChunkDataHC

chunkqueue = queue.Queue()

with open("mn2mc/mini/airchunk", "rb") as f:
    air = f.read()


def on_recv(client: MCClient, chunklist: list, metadata: dict):
    for chunkdata in chunklist:
        chunkqueue.put((client, chunkdata))


def send_air_chunk(client: MCClient, jsondata: dict):
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


def parse_done(client: MCClient, chunkdata: dict):
    send_air_chunk(client, chunkdata)
    converted_blocks = []
    blocksex = []
    blockstates = []
    for block in chunkdata["blocks"]:
        if block[3] != 0:
            blockid = block_mapping.mc_to_mini(block[3])
            encoded, quotient = mini_block.encode_block(
                blockid, 15 - block[0], block[1], block[2]
            )
            converted_blocks.append(encoded)
            blocksex.append(quotient)
            if len(block) == 5:
                blockstates.append(block_face_mapping.get_block_face(blockid, block[4]))
            else:
                blockstates.append(0)
            if len(blocksex) % 6000 == 0:
                send_blocks(
                    client.miniplayer,
                    -chunkdata["x"] - 1,
                    chunkdata["z"],
                    converted_blocks,
                    blocksex,
                    blockstates,
                )
                converted_blocks.clear()
                blocksex.clear()

    send_blocks(
        client.miniplayer,
        -chunkdata["x"] - 1,
        chunkdata["z"],
        converted_blocks,
        blocksex,
        blockstates,
    )
    del converted_blocks
    del blocksex


def send_blocks(
    miniplayer: MiniPlayer,
    x: int,
    z: int,
    converted_blocks: list,
    blocksex: list,
    blockstates: list,
):
    miniplayer.send_packet(
        ePBMsgCode.PB_BLOCK_DATA_UPDATE_HC,
        PB_BlockUpdateHC(
            ChunkX=x,
            ChunkZ=z,
            MapID=0,
            Blocks=converted_blocks,
            BlocksEx=blocksex,
            BlockStateIndex=blockstates,
        ).SerializeToString(),
    )


def chunk_parse_thread():
    while mn2mc.running:
        try:
            data = chunkqueue.get()
            parse_done(data[0], data[1])
        except queue.ShutDown:
            return


for i in range(config.mc["chunk_parse_thread"]):
    threading.Thread(
        target=chunk_parse_thread, name=f"Chunk parser {i}", daemon=True
    ).start()


def stop():
    chunkqueue.shutdown()


add_event("parsed_chunk", on_recv)

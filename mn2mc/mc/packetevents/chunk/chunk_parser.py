"""Shared chunk parsing utilities for MC→Mini World block conversion.

Extracted from map_chunk.py and parsed_chunk.py to eliminate duplication.
Both parsers import from this module for common operations.
"""

from __future__ import annotations

import queue
import threading
from typing import TYPE_CHECKING

import mn2mc
import mn2mc.config as config
import mn2mc.mapping.block_face as block_face_mapping
import mn2mc.mapping.blocks as block_mapping
import mn2mc.utils.mini_block as mini_block
from mn2mc.constants import SECTION_FLAGS
from mn2mc.mini.proto.common import PB_ChunkBlob, PB_ChunkSaveDB, ePBMsgCode
from mn2mc.mini.proto.hc import PB_BlockUpdateHC, PB_SyncChunkDataHC

if TYPE_CHECKING:
    from mn2mc.mini.player import MiniPlayer

# Air chunk data loaded once at module level
with open("mn2mc/mini/airchunk", "rb") as f:
    air = f.read()

# Default OWID for chunk packets (from Mini World protocol)
_DEFAULT_OWID = 10239475674329


def send_air_chunk(miniplayer: MiniPlayer, x: int, z: int):
    """Send an empty air chunk to the Mini World client.

    Args:
        miniplayer: MiniPlayer to send to
        x: Chunk X coordinate (already adjusted, e.g. -jsondata["x"] - 1)
        z: Chunk Z coordinate
    """
    minichunk = PB_SyncChunkDataHC(
        SectionFlags=SECTION_FLAGS,
        Initialize=1,
        ChunkData=PB_ChunkSaveDB(
            OWID=_DEFAULT_OWID,
            MapID=0,
            x=x,
            z=z,
            ChunkBlob=PB_ChunkBlob(UnzipLen=805308264, BlobLen=554, BlobDetail=air),
        ),
    ).SerializeToString()
    miniplayer.send_packet(ePBMsgCode.PB_SYNC_CHUNK_DATA_HC, minichunk)


def send_blocks(
    miniplayer: MiniPlayer,
    x: int,
    z: int,
    converted_blocks: list,
    blocksex: list,
    blockstates: list,
):
    """Send converted block data to the Mini World client."""
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


def send_block_updates(
    miniplayer: MiniPlayer,
    x: int,
    z: int,
    blocks: list,
    flush_threshold: int = 2048,
):
    """Convert MC blocks to Mini World format and send in batches.

    Args:
        miniplayer: MiniPlayer instance to send blocks to
        x: Chunk X coordinate (already negated/adjusted)
        z: Chunk Z coordinate
        blocks: List of block data [x, y, z, type] or [x, y, z, type, properties]
        flush_threshold: Number of blocks to batch before sending intermediate update
    """
    converted_blocks = []
    blocksex = []
    blockstates = []
    for block in blocks:
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
            if len(blocksex) % flush_threshold == 0:
                send_blocks(miniplayer, x, z, converted_blocks, blocksex, blockstates)
                converted_blocks.clear()
                blocksex.clear()

    send_blocks(miniplayer, x, z, converted_blocks, blocksex, blockstates)
    del converted_blocks
    del blocksex


def create_worker_threads(process_func, chunkqueue, thread_count=None):
    """Create and start chunk parse worker threads.

    Args:
        process_func: Function to call with (client, chunkdata) from queue
        chunkqueue: Queue to read from
        thread_count: Number of threads (defaults to config value)
    """
    if thread_count is None:
        thread_count = config.mc["chunk_parse_thread"]

    def _parse_thread():
        while mn2mc.running:
            try:
                data = chunkqueue.get()
                process_func(data)
            except queue.ShutDown:
                return

    for i in range(thread_count):
        threading.Thread(
            target=_parse_thread, name=f"Chunk parser {i}", daemon=True
        ).start()

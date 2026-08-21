"""Shared chunk parsing utilities for MC→Mini World block conversion.

Extracted from map_chunk.py and parsed_chunk.py to eliminate duplication.
Both parsers import from this module for common operations.
"""

from __future__ import annotations

import queue
import threading
import time
from typing import TYPE_CHECKING

from loguru import logger

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


def send_fast_chunk(
    miniplayer: MiniPlayer,
    x: int,
    z: int,
    blocks: list,
    lights: list | None = None,
    light_flag: int = 0,
):
    """Build a real 1.58 PalettedTable chunk and send it to the Mini World client.

    Replaces the slow path (air chunk + per-block updates) when
    ``config.mc.fast_chunk_conversion`` is enabled. The chunk is built with
    ``mn2mc.mini.chunk.chunk_builder_158`` (real 1.58 on-disk format),
    zstd compressed and sent as a single ``PB_SYNC_CHUNK_DATA_HC``.

    Args:
        miniplayer: MiniPlayer to send to
        x: Chunk X coordinate (already adjusted, e.g. -chunkdata["x"] - 1)
        z: Chunk Z coordinate
        blocks: List of block data [x, y, z, type] or [x, y, z, type, properties]
        lights: Optional MC per-section light data from chunk.js:
            [{sec_y, sky?, block?}] with 2048-byte nibble arrays. Written into
            the container-f1 light table (real MC light). None → no light table
            (client renders the chunk dark).
        light_flag: Light flag u16 passed through to each section (default 0)
    """
    from mn2mc.mini.chunk.chunk_builder_158 import (
        BLOCKS_PER_SECTION,
        CHUNK_DATA_VERSION_158_0,
        build_full_chunk_158,
        compress_chunk_158,
    )

    ts = time.monotonic()
    # Use the MC per-section light data as-is (real sky/block light from
    # chunk.js). Writing the container-f1 light table makes the client render
    # light; absent table → empty light layers, dark chunk.
    light = _mc_lights_to_table(lights) if lights else None
    if light:
        # MC light is packed at MC x; blocks are stored x-flipped (15-x), so
        # flip light X too or it renders mirrored (light4.txt: 550 at local
        # x=8..15, light 15 at 15-x=7..0).
        for sec_y in list(light["sky"]):
            light["sky"][sec_y] = _flip_light_x(light["sky"][sec_y])
        for blk in light["block"]:
            for sec_y in list(blk):
                blk[sec_y] = _flip_light_x(blk[sec_y])
    # Group MC blocks into 16x16x16 sections. The x axis is flipped to match
    # the slow path's coordinate convention (encode_block(15 - x, ...)).
    sections: dict[int, dict] = {}
    for block in blocks:
        if block[3] == 0:
            continue
        bx, by, bz, mctype = block[0], block[1], block[2], block[3]
        mini_id = block_mapping.mc_to_mini(mctype)
        sec_y = by // 16
        # get-or-create, NOT setdefault: setdefault eagerly evaluates its
        # default argument, so the two 4096-element lists + dict below would be
        # allocated on EVERY block (even for existing sections) — ~250ms/chunk.
        sec = sections.get(sec_y)
        if sec is None:
            sec = {
                "sec_y": sec_y,
                "blocks": [0] * BLOCKS_PER_SECTION,
                "states": [0] * BLOCKS_PER_SECTION,
            }
            sections[sec_y] = sec
        idx = (15 - bx) + bz * 16 + (by % 16) * 256
        sec["blocks"][idx] = mini_id
        if len(block) == 5:
            sec["states"][idx] = block_face_mapping.get_block_face(mini_id, block[4])
    # Always emit all 16 sections. The Mini World client MERGES the incoming
    # chunk into the one it already holds for this position, so a reloaded
    # chunk with fewer sections leaves the old ones visible (stale terrain).
    # Filling missing sections with air forces a full replacement; an all-air
    # section is cheap (single-entry palette, no packed data).
    for sy in range(16):
        if sy not in sections:
            sections[sy] = {"sec_y": sy, "blocks": [0] * BLOCKS_PER_SECTION, "states": [0] * BLOCKS_PER_SECTION}
    raw = build_full_chunk_158(
        [sec for _, sec in sorted(sections.items())],
        data_version=CHUNK_DATA_VERSION_158_0,
        light=light,
    )
    compressed, unzip_len = compress_chunk_158(raw)
    minichunk = PB_SyncChunkDataHC(
        SectionFlags=SECTION_FLAGS,
        Initialize=1,
        ChunkData=PB_ChunkSaveDB(
            OWID=_DEFAULT_OWID,
            MapID=0,
            x=x,
            z=z,
            ChunkBlob=PB_ChunkBlob(UnzipLen=unzip_len, BlobLen=len(compressed), BlobDetail=compressed),
        ),
    ).SerializeToString()
    #logger.debug(f"build chunk cost {(time.monotonic() - ts) * 1000}ms")
    miniplayer.send_packet(ePBMsgCode.PB_SYNC_CHUNK_DATA_HC, minichunk)


# byte → nibble-swapped byte: (hi,lo) → (lo,hi). Used by _flip_light_x where
# each flipped row is a byte reversal combined with a per-byte nibble swap.
_NIBBLE_SWAP_LUT = bytes(((i & 0x0F) << 4) | (i >> 4) for i in range(256))


def _flip_light_x(nibbles_2048: bytes) -> bytes:
    """X-flip a 2048-byte light nibble array (4096 nibbles, linear x + z*16 + y*256).

    chunk.js packs MC light at MC x; send_fast_chunk stores blocks x-flipped
    (15-x), so light must be flipped too or it renders mirrored in X.
    """
    # The flip maps x → 15-x within each 16-nibble row. A row's 8 bytes are
    # reversed AND nibble-swapped per byte (output byte j = swap(input byte
    # 7-j)), so translate + per-row reverse replaces the per-nibble loop.
    swapped = nibbles_2048.translate(_NIBBLE_SWAP_LUT)
    out = bytearray(2048)
    for r in range(256):
        base = r * 8
        out[base : base + 8] = swapped[base : base + 8][::-1]
    return bytes(out)


def _mc_lights_to_table(lights: list) -> dict:
    """Convert MC per-section light data to a build_full_chunk_158 light dict.

    chunk.js extracts per-section sky/block light as 2048-byte nibble arrays
    (already in Mini World linear layout). The builder's light dict wants
    {"sky": {sec_y: bytes}, "block": [{sec_y: bytes}]} — MC has a single
    white block-light channel, so R = G = B (len 1 → builder triplicates).

    Args:
        lights: [{sec_y, sky?, block?}] with 2048-byte nibble arrays.

    Returns:
        Light dict accepted by build_full_chunk_158's ``light`` parameter.
    """
    sky: dict[int, bytes] = {}
    block: dict[int, bytes] = {}
    for light in lights:
        sec_y = light.get("sec_y", 0)
        if light.get("sky") is not None:
            sky[sec_y] = light["sky"]
        if light.get("block") is not None:
            block[sec_y] = light["block"]
    return {"sky": sky, "block": [block]}


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
            encoded, quotient = mini_block.encode_block(blockid, 15 - block[0], block[1], block[2])
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
        thread_count = config.mc.chunk_parse_thread

    def _parse_thread():
        while mn2mc.running:
            try:
                data = chunkqueue.get(timeout=0.5)
                process_func(data)
            except queue.Empty:
                continue
            except queue.ShutDown:
                return

    for i in range(thread_count):
        threading.Thread(target=_parse_thread, name=f"Chunk parser {i}", daemon=True).start()


def stop_chunk_workers() -> None:
    """Shut down the active chunk parse queue (idempotent)."""
    if config.mc.use_new_chunk_parser:
        from mn2mc.mc.packetevents.chunk import parsed_chunk

        parsed_chunk.stop()
    else:
        from mn2mc.mc.packetevents.chunk import map_chunk

        map_chunk.stop()

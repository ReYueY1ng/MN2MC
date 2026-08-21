from __future__ import annotations

from loguru import logger

import mn2mc.config as config
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents.chunk.chunk_parser import _DEFAULT_OWID, _flip_light_x
from mn2mc.mini.proto.common import PB_SectionLightData, PB_SectionLightDB, ePBMsgCode
from mn2mc.mini.proto.hc import PB_SyncSectionLightDataHC

# Mini World chunks are 256 blocks tall (16 sections); MC sections outside
# sec_y 0..15 (e.g. an overworld's -64..-1 bedrock layer) have no Mini
# counterpart and are dropped.
_VALID_SEC_Y = frozenset(range(16))

_ZERO_LIGHT = bytes(2048)


def _varint(n: int) -> bytes:
    out = bytearray()
    while n > 0x7F:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    out.append(n)
    return bytes(out)


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Translate MC update_light into Mini World section light updates.

    chunk.js pre-computes ``jsondata["_secY"]`` from the packet's light masks
    (it owns minY): {"sky": [sec_y...], "block": [sec_y...],
    "skyClear": [sec_y...], "blockClear": [sec_y...]}. The sky/block lists map
    1:1 (in mask bit order) to the packet's skyLight/blockLight u8[2048]
    arrays; sections in the *_Clear masks carry NO data — their light was
    zeroed server-side and must be cleared on the client too.

    Per section, each channel is handled in three states:
      - in a data mask   -> send the (x-flipped) light data
      - in a clear mask  -> send all-zero data (client clears old light)
      - in neither       -> omit the layer (client keeps the old value)
    """
    if not config.mc.fast_chunk_conversion:
        return
    sec_y_map = jsondata.get("_secY")
    if not sec_y_map:
        return
    sky_bits = sec_y_map.get("sky", [])
    block_bits = sec_y_map.get("block", [])
    sky_clear = set(sec_y_map.get("skyClear", []))
    block_clear = set(sec_y_map.get("blockClear", []))

    cx = -jsondata["chunkX"] - 1
    cz = jsondata["chunkZ"]

    from mn2mc.mini.chunk.section_light_blob_builder import (
        build_section_light_blob,
        compress_section_light_blob,
    )

    sky_list = jsondata.get("skyLight") or []
    block_list = jsondata.get("blockLight") or []
    # Blocks are stored x-flipped in send_fast_chunk, and its light was
    # flipped to match — server light here is at MC x, so flip it too or the
    # update renders mirrored.
    sky_data: dict[int, bytes] = {
        sy: _flip_light_x(bytes(sky_list[i]))
        for i, sy in enumerate(sky_bits)
        if i < len(sky_list) and sy in _VALID_SEC_Y
    }
    block_data: dict[int, bytes] = {
        sy: _flip_light_x(bytes(block_list[i]))
        for i, sy in enumerate(block_bits)
        if i < len(block_list) and sy in _VALID_SEC_Y
    }

    for sec_y in sorted((set(sky_data) | set(block_data) | sky_clear | block_clear) & _VALID_SEC_Y):
        sky = sky_data.get(sec_y) if sec_y in sky_data else (_ZERO_LIGHT if sec_y in sky_clear else None)
        block = block_data.get(sec_y) if sec_y in block_data else (_ZERO_LIGHT if sec_y in block_clear else None)
        try:
            raw = build_section_light_blob(sky, block, omit_empty=False)
        except ValueError as e:
            logger.warning(f"update_light: bad section light ({sec_y}): {e}")
            continue
        compressed, unzip_len = compress_section_light_blob(raw)
        # LightDataDetail is a string-typed proto field holding raw zstd bytes.
        # Field assignment enforces utf-8, but ParseFromString does not — build
        # the inner wire manually so arbitrary binary survives byte-exact.
        light_data = PB_SectionLightData()
        light_data.ParseFromString(
            b"\x08"
            + _varint(unzip_len)
            + b"\x10"
            + _varint(len(compressed))
            + b"\x1a"
            + _varint(len(compressed))
            + compressed
        )
        msg = PB_SyncSectionLightDataHC(
            SectionLightData=PB_SectionLightDB(
                OWID=_DEFAULT_OWID,
                MapID=0,
                x=cx,
                z=cz,
                y=sec_y,
                SectionLightData=light_data,
            ),
        ).SerializeToString()
        client.miniplayer.send_packet(ePBMsgCode.PB_SYNC_SECTION_LIGHT_DATA_HC, msg)


add_event("update_light", on_recv)

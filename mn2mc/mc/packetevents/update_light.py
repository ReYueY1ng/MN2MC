from __future__ import annotations

from loguru import logger

import mn2mc.config as config
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents.chunk.chunk_parser import _DEFAULT_OWID
from mn2mc.mini.proto.common import PB_SectionLightData, PB_SectionLightDB, ePBMsgCode
from mn2mc.mini.proto.hc import PB_SyncSectionLightDataHC


def _varint(n: int) -> bytes:
    out = bytearray()
    while n > 0x7F:
        out.append((n & 0x7F) | 0x80)
        n >>= 7
    out.append(n)
    return bytes(out)


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Translate MC update_light into Mini World section light updates.

    chunk.js pre-computes ``jsondata["_secY"]`` = {"sky": [sec_y...],
    "block": [sec_y...]} from the packet's light masks (it owns minY).
    Each masked section maps 1:1 (in mask bit order) to the packet's
    skyLight/blockLight u8[2048] arrays.
    """
    if not config.mc.fast_chunk_conversion:
        return
    logger.debug(jsondata)
    sec_y_map = jsondata.get("_secY")
    if not sec_y_map:
        return
    sky_bits = sec_y_map.get("sky", [])
    block_bits = sec_y_map.get("block", [])
    if not sky_bits and not block_bits:
        return

    cx = -jsondata["chunkX"] - 1
    cz = jsondata["chunkZ"]

    from mn2mc.mini.chunk.section_light_blob_builder import (
        build_section_light_blob,
        compress_section_light_blob,
    )

    sky_list = jsondata.get("skyLight") or []
    block_list = jsondata.get("blockLight") or []
    sky_by_sec: dict[int, bytes] = {
        sy: bytes(sky_list[i]) for i, sy in enumerate(sky_bits) if i < len(sky_list)
    }
    block_by_sec: dict[int, bytes] = {
        sy: bytes(block_list[i]) for i, sy in enumerate(block_bits) if i < len(block_list)
    }

    for sec_y in sorted(set(sky_by_sec) | set(block_by_sec)):
        sky = sky_by_sec.get(sec_y, bytes(2048))
        block = block_by_sec.get(sec_y, bytes(2048))
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
            b"\x08" + _varint(unzip_len)
            + b"\x10" + _varint(len(compressed))
            + b"\x1a" + _varint(len(compressed)) + compressed
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

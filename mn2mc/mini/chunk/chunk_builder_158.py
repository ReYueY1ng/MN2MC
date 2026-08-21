"""
FlatBuffer chunk builder for Mini World v1.58 PalettedTable format.

Builds the REAL 1.58 on-disk chunk format (verified against actual saves
from 1.58.0/1.58.2 worlds, parsed by the GUI satellite-tool logic):

    root (16 fields)
      └─ f15 (tag 34) = section container table (7 fields)
           ├─ f1 (tag  6) = light table (4 layers × 18 element tables)
           └─ f2 (tag  8) = sections vector [uoffset...]
                └─ section table (6+ fields)
                     ├─ f0 (tag  4) = sec_y (u32)
                     ├─ f1 (tag  6) = data vector (packed 64-bit words)
                     ├─ f2 (tag  8) = palette vector [uoffset → PaletteEntry]
                     ├─ f3 (tag 10) = blockCount (u16, non-air count)
                     └─ f4 (tag 12) = lightFlag (u16)
                          └─ PaletteEntry.f0 = block_id (u32)
                          └─ PaletteEntry.f1 = state vector [uoffset → StateTable]
                               ├─ StateTable.f0 = state hash (u32)
                               └─ StateTable.f2 = block data value (u32)

Lighting (container.f1, see RE/1.58_light_data.md):
    light table (4 fields, tags 4/6/8/10 = sky / block R / block G / block B)
      └─ each layer = vector of 18 element tables:
           [0]   header (f1 flag = 2)
           [1..16] sections sec_y 0..15 (f0 = u8[2048] nibble data, f1 flag = 1)
           [17]  spare
    pass light="auto" (compute from blocks) or an explicit dict to
    build_full_chunk_158; absent light → game loads empty light layers.

Data packing (matches GUI ChunkView):
  bits_per_entry = max(4, (palette_size - 1).bit_length())
  values_per_word = 64 // bits_per_entry
  linear = lx + lz*16 + ly*256
  words  = ceil(4096 / values_per_word) * 8 bytes (e.g. 2048 B for 4 bits)
  palette_size <= 1 and data_length == 0  →  whole section implicitly palette[0]

Wire format: standard FlatBuffer (vsize-first vtables, direct uoffsets).

References:
  - RE/1.58_world_analysis.md (real-save analysis)
  - GUI satellite-tool core miniworld_core.py (RegionFile/ChunkView/FlatBufferView)
  - RE/1.58_writer_pipeline.md (IDA decompile of buildChunkFlatBuffer)
"""

import struct
import threading
from dataclasses import dataclass
from dataclasses import field as dc_field
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, TypedDict, Union

try:  # package import (mn2mc.mini.chunk)
    from .block_state_hashes import state_hash_for
    from .minimal_chunk_builder import _mk_vector, _mk_vtable_std
except ImportError:  # standalone script execution
    from block_state_hashes import state_hash_for
    from minimal_chunk_builder import _mk_vector, _mk_vtable_std

BLOCKS_PER_SECTION = 16 * 16 * 16  # 4096

# Real on-disk data_version values (root.f11 / tag 26), measured from actual
# 1.58.0/1.58.2 saves. Encoding: (major << 8) | minor — 0x13A00 = major 0x13A,
# minor 0 (1.58.0) / 2 (1.58.2). NEVER 0: the writer always emits a non-zero
# data version, and 0 is not a value any real save carries.
CHUNK_DATA_VERSION_158_0 = 0x13A00  # 80384  — 1.58.0 saves
CHUNK_DATA_VERSION_158_2 = 0x13A02  # 80386  — 1.58.2 saves

# ============================================================================
# Light (container.f1 light table) — 1.58 PalettedTable lighting
# ============================================================================

# Light-layer indices inside the container.f1 light table (4-field table,
# tags 4/6/8/10 → f0..f3). Semantics reverse-engineered from real 1.58.0/2
# saves (RE/1.58_light_data.md):
#   f0 = SKY light     (15 above ground, attenuated by block LightAtten)
#   f1 = BLOCK light R (emitter LightSrc minus Manhattan distance)
#   f2 = BLOCK light G
#   f3 = BLOCK light B
# White light sources store identical values in f1/f2/f3 (R=G=B); real saves
# show this: the three block channels are byte-identical for torch/lava light.
LIGHT_LAYER_SKY = 0
LIGHT_LAYER_BLOCK_R = 1
LIGHT_LAYER_BLOCK_G = 2
LIGHT_LAYER_BLOCK_B = 3

# A light-table layer is a vector of 18 element tables (measured from real
# 1.58.0/1.58.2 saves; writer = LightSectionsBuilder @0x1807FB320):
#   [0]     header element: f1 u32 flag = 2, no data vector.
#           Present in every layer whenever the chunk carries ANY light data;
#           absent (empty table) when the chunk has no light at all.
#   [1..16] sections sec_y 0..15. A section WITH light data:
#             f0 = u8[2048] nibble vector (4096 nibbles), f1 u32 flag = 1.
#           A section WITHOUT light data: empty 2-slot table (no fields).
#   [17]    spare/terminator: empty table.
# Element vtable shapes (real bytes):
#   data-bearing: 08 00 0c 00 04 00   (vsize 8, tsize 12, foffs [4,8])
#   header:       08 00 08 00 00 00   (vsize 8, tsize  8, foffs [0,4])
#   empty:        08 00 04 00 00 00   (vsize 8, tsize  4, foffs [0,0])
LIGHT_ELEMENTS = 18
LIGHT_HEADER_FLAG = 2
LIGHT_SECTION_FLAG = 1
LIGHT_NIBBLES_PER_SECTION = 16 * 16 * 16  # 4096
LIGHT_BYTES_PER_SECTION = LIGHT_NIBBLES_PER_SECTION // 2  # 2048


def light_flag_for_section_158(n_light_sources: int, has_sky_light: bool = False) -> int:
    """Build a lightFlag value matching real 1.58 saves (RE/1.58_light_data.md §6).

    Reverse-engineered from 37k+ real sections: the low byte is the number
    of light-emitting blocks (LightSrc > 0) in the section (mod 256); the
    high byte is the light-channel state flag the light engine recorded on
    its last propagation pass — 0x0300 for sky-lit sections, 0x0400-family
    for block-lit ones. Real values combine them: 1.58.0 sec0 = 0x0309
    (sky + 9 sources). The flag is persisted but the reader only stores it,
    so 0 remains safe; this helper reproduces the common real-save pattern.

    Args:
        n_light_sources: count of light-emitting blocks (0..255 used; mod 256).
        has_sky_light: True → add the 0x0300 sky-channel flag.

    Returns:
        The lightFlag u16.
    """
    flag = 0x0300 if has_sky_light else 0
    return flag | (n_light_sources & 0xFF)


def pack_nibbles_158(values: Union[bytes, List[int]]) -> bytes:
    """Pack 4096 nibble values (0..15) into 2048 bytes, low nibble first.

    Matches the game's NibbleArray byte layout: value 2i in the low nibble
    of byte i, value 2i+1 in the high nibble (real-save verified).

    Args:
        values: 4096 ints in [0, 15], or 2048 raw packed bytes (passthrough).

    Returns:
        2048 packed bytes.

    Raises:
        ValueError: If values is a list of the wrong length or out of range.
    """
    if isinstance(values, (bytes, bytearray)):
        if len(values) != LIGHT_BYTES_PER_SECTION:
            raise ValueError(f"packed light data must be {LIGHT_BYTES_PER_SECTION} bytes, got {len(values)}")
        return bytes(values)
    if len(values) != LIGHT_NIBBLES_PER_SECTION:
        raise ValueError(f"light nibbles must have {LIGHT_NIBBLES_PER_SECTION} entries, got {len(values)}")
    out = bytearray(LIGHT_BYTES_PER_SECTION)
    for i, v in enumerate(values):
        v = int(v)
        if not (0 <= v <= 0xF):
            raise ValueError(f"light nibble {v} out of range [0, 15]")
        if i % 2 == 0:
            out[i // 2] |= v
        else:
            out[i // 2] |= v << 4
    return bytes(out)


def _mk_light_element_158(data: Optional[Union[bytes, List[int]]], flag: int) -> bytes:
    """Build one light-layer element table (2-slot).

    Wire shapes (matching real saves byte-for-byte):
      data + flag → [soffset][f0 uoff @+4][f1 u32 @+8][u8[2048] vec]
                     vtable 08 00 0c 00 04 00  (tsize 12)
      flag only    → [soffset][f1 u32 @+4]      vtable 08 00 08 00 00 00  (tsize 8)
      neither      → [soffset]                  vtable 08 00 04 00 00 00  (tsize 4)
    """
    if data is not None:
        data = pack_nibbles_158(data)
        buf = bytearray()
        buf.extend(b"\x00\x00\x00\x00")  # soffset placeholder
        buf.extend(b"\x00\x00\x00\x00")  # f0 uoff @+4
        buf.extend(struct.pack("<I", flag & 0xFFFFFFFF))  # f1 @+8
        vec_pos = len(buf)  # 12
        buf.extend(struct.pack("<I", len(data)))
        buf.extend(data)
        struct.pack_into("<I", buf, 4, vec_pos - 4)  # f0 uoff → vector
        vtbl = _mk_vtable_std([4, 8], 4 + 12)
        vtbl_pos = len(buf)
        buf.extend(vtbl)
        struct.pack_into("<i", buf, 0, -vtbl_pos)
        return bytes(buf)
    if flag:
        return _mk_table([0, 4], struct.pack("<I", flag & 0xFFFFFFFF))
    return _mk_table([0, 0], b"")


def build_light_layer_158(
    sections_light: Mapping[int, Optional[Union[bytes, List[int]]]],
    has_chunk_light: bool,
) -> bytes:
    """Build one layer vector: 18 element tables (header + 16 + spare).

    Args:
        sections_light: sec_y (0..15) → 2048 packed bytes / 4096 nibbles,
            or None / missing for sections without light data.
        has_chunk_light: True → header element carries flag 2 (matches real
            saves whenever any layer of the chunk holds light data).

    Returns:
        FlatBuffer vector bytes ([u32 count][uoffset...][element tables]).
    """
    elements: List[Tuple[Optional[Union[bytes, List[int]]], int]] = []
    # el[0] header
    elements.append((None, LIGHT_HEADER_FLAG) if has_chunk_light else (None, 0))
    # el[1..16] sections sec_y 0..15
    for sy in range(16):
        d = sections_light.get(sy)
        elements.append((d, LIGHT_SECTION_FLAG) if d is not None else (None, 0))
    # el[17] spare
    elements.append((None, 0))

    buf = bytearray()
    vec_pos = len(buf)
    buf.extend(struct.pack("<I", len(elements)))
    for _ in elements:
        buf.extend(b"\x00\x00\x00\x00")
    el_positions: List[int] = []
    for d, flag in elements:
        el_positions.append(len(buf))
        buf.extend(_mk_light_element_158(d, flag))
    for i, ep in enumerate(el_positions):
        slot = vec_pos + 4 + i * 4
        struct.pack_into("<I", buf, slot, ep - slot)
    return bytes(buf)


def build_light_table_158(
    sky: Mapping[int, Optional[Union[bytes, List[int]]]],
    block: Optional[Sequence[Mapping[int, Optional[Union[bytes, List[int]]]]]] = None,
) -> bytes:
    """Build the container.f1 light table (4-field table, tags 4/6/8/10).

    Args:
        sky: per-section sky light (layer f0).
        block: optional list of 1 or 3 per-section block-light dicts.
            len 1 → white light (f1=f2=f3 identical, like real saves).
            len 3 → RGB channels (f1, f2, f3). Default: all-empty layers.
            Each dict: sec_y → packed bytes / 4096 nibbles, or None.

    Returns:
        The 4-field light table bytes (self-contained table).

    Raises:
        ValueError: If block is not length 1 or 3.
    """
    if block is None:
        block = [{}]
    block = list(block)
    if len(block) == 1:
        block = block * 3  # white light: R = G = B
    if len(block) != 3:
        raise ValueError(f"block light must be 1 or 3 channels, got {len(block)}")

    has_light = bool(any(v is not None for v in sky.values()) or any(v is not None for c in block for v in c.values()))

    layer_bytes = [
        build_light_layer_158(sky, has_light),
        build_light_layer_158(block[0], has_light),
        build_light_layer_158(block[1], has_light),
        build_light_layer_158(block[2], has_light),
    ]

    # table: [soffset][inline 4×u32 uoffsets][layer vectors][vtable]
    buf = bytearray()
    stbl_pos = len(buf)
    buf.extend(b"\x00\x00\x00\x00")  # soffset placeholder
    buf.extend(b"\x00" * 16)  # 4 uoffset fields @+4..+16
    vec_offsets: List[int] = []
    for layer in layer_bytes:
        vec_offsets.append(len(buf))
        buf.extend(layer)
    for i, vo in enumerate(vec_offsets):
        field_pos = stbl_pos + 4 + i * 4
        struct.pack_into("<I", buf, field_pos, vo - field_pos)
    vtbl = _mk_vtable_std([4, 8, 12, 16], 4 + 16)
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, stbl_pos, stbl_pos - vtbl_pos)
    return bytes(buf)


# ----------------------------------------------------------------------------
# Light computation (blockdef LightAtten / LightSrc physics)
# ----------------------------------------------------------------------------
# Calibrated against real_chunk_158_0.bin (RE/1.58_light_data.md):
#   SKY light:   value = 15 at the top boundary, each block reduces the light
#                passing through it by its LightAtten (blockdef '光衰减').
#                Air (atten 0) transmits unchanged → 15 across open sky;
#                stone/grass (atten 15) → 0; water (atten 1) → 14;
#                ice (atten 3) → 12. Verified: block 150902 (atten 1) → 14.
#   BLOCK light: emitters (blockdef '光源强度' LightSrc) radiate with
#                value = min(15, LightSrc), decreasing by 1 per Manhattan
#                step; opaque blocks (atten >= 15) block propagation.
#                Verified: source block → 10, air at distance d → 10-d,
#                ice 9 steps away → 1.

# Built-in LightAtten defaults for common blocks (blockdef.csv column 34).
# Unknown block types are treated as opaque (15) — matches real terrain
# saves (stone/dirt/grass are all 15).
DEFAULT_LIGHT_ATTEN: Dict[int, int] = {
    0: 0,  # 空气 air
    3: 1,  # 静态水
    4: 1,  # 水
    5: 0,  # 静态岩浆 (transmits light like air)
    6: 0,  # 岩浆
    9: 0,  # 地心传送门方块
    12: 1,  # 蜂蜜
    113: 3,  # 浮冰
    123: 3,  # 冰
    218: 10,
    219: 10,
    220: 10,
    221: 10,
    222: 10,
    223: 10,  # 树叶 (all leaves)
    224: 0,
    225: 0,
    234: 0,  # 小草/枯草/水稻
}

# Built-in LightSrc defaults for common emitters (blockdef.csv column 35).
# Unknown blocks emit no light.
DEFAULT_LIGHT_SRC: Dict[int, int] = {
    5: 15,  # 静态岩浆
    6: 15,  # 岩浆
    9: 15,  # 地心传送门方块
    132: 15,  # 硫黄晶砂
    244: 15,  # 圣诞树
    500: 15,  # 火
    536: 15,  # 曙光石块
    550: 15,  # 荧光晶块
    580: 15,  # 祭台
    581: 15,  # 天气预报器
    584: 15,  # 毒液
    591: 15,
    593: 15,
    594: 15,  # 神圣树-树苗/核心, 星站-控制台
    687: 15,  # 香薰宫灯
    708: 15,  # 电石信号灯
    732: 15,
    740: 15,
    741: 15,
    742: 15,
    746: 15,  # 龙雕像/龙蛋
    1146: 30,  # 庆典花灯 (5-bit source; clamped to 15 in the 4-bit layer)
}

_WORLD_HEIGHT = 256  # 16 sections × 16


def load_blockdef_light_maps(csv_path: str) -> Tuple[Dict[int, int], Dict[int, int]]:
    """Parse a blockdef.csv into (LightAtten, LightSrc) maps by block type id.

    blockdef.csv is the game's authoritative block table (csvdef/utf8/
    blockdef.csv). Columns are located by their English header names
    ('ID', 'LightAtten', 'LightSrc') so the parser survives column shifts.
    """
    import csv

    atten: Dict[int, int] = {}
    src: Dict[int, int] = {}
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        next(reader, None)  # Chinese header row
        header = next(reader, None)  # English header row
        if header is None:
            raise ValueError(f"blockdef.csv has no header: {csv_path}")
        idx = {name: i for i, name in enumerate(header)}
        if "ID" not in idx or "LightAtten" not in idx or "LightSrc" not in idx:
            raise ValueError(f"blockdef.csv missing ID/LightAtten/LightSrc columns: {csv_path}")
        for row in reader:
            if not row or not row[idx["ID"]].strip().isdigit():
                continue
            bid = int(row[idx["ID"]])
            a = row[idx["LightAtten"]].strip()
            s = row[idx["LightSrc"]].strip()
            if a.isdigit():
                atten[bid] = int(a)
            if s.isdigit() and int(s) > 0:
                src[bid] = int(s)
    return atten, src


def compute_sky_light_158(
    sections: List[dict],
    atten: Optional[Dict[int, int]] = None,
) -> Dict[int, Optional[bytes]]:
    """Compute per-section sky light (4096 nibbles → 2048 packed bytes).

    Flood-fill from the world top (y=255): value 15, each block reduces the
    incoming light by its LightAtten. Air (atten 0) transmits unchanged, so
    open sky is 15 and stone (atten 15) is 0 — matching real saves. Light
    also propagates horizontally (cave entrances stay lit).

    Args:
        sections: list of {"sec_y", "blocks"}; missing sections = air.
        atten: block-type → LightAtten (default DEFAULT_LIGHT_ATTEN +
            opaque fallback for unknown types).

    Returns:
        sec_y → 2048 packed bytes for sections with any non-zero light,
        None for all-zero sections (written as empty element tables).
    """
    if atten is None:
        atten = DEFAULT_LIGHT_ATTEN
    blocks = _world_block_grid(sections)
    light = [0] * (16 * 16 * _WORLD_HEIGHT)

    def _idx(x: int, z: int, y: int) -> int:
        return x + z * 16 + y * 256

    def _atten(x: int, z: int, y: int) -> int:
        return atten.get(blocks[_idx(x, z, y)] & 0xFFF, 15)

    from collections import deque

    queue: deque = deque()
    for x in range(16):
        for z in range(16):
            y = _WORLD_HEIGHT - 1
            v = 15 - _atten(x, z, y)
            if v < 0:
                v = 0
            i = _idx(x, z, y)
            if v > light[i]:
                light[i] = v
                if v > 0:
                    queue.append(i)
    while queue:
        i = queue.popleft()
        x, z, y = i % 16, (i // 16) % 16, i // 256
        L = light[i]
        for nx, nz, ny in ((x - 1, z, y), (x + 1, z, y), (x, z - 1, y), (x, z + 1, y), (x, z, y - 1), (x, z, y + 1)):
            if not (0 <= nx < 16 and 0 <= nz < 16 and 0 <= ny < _WORLD_HEIGHT):
                continue
            v = L - _atten(nx, nz, ny)
            if v < 0:
                v = 0
            ni = _idx(nx, nz, ny)
            if v > light[ni]:
                light[ni] = v
                if v > 0:
                    queue.append(ni)

    return _section_nibbles(light, sections)


def compute_block_light_158(
    sections: List[dict],
    atten: Optional[Dict[int, int]] = None,
    src: Optional[Dict[int, int]] = None,
) -> Dict[int, Optional[bytes]]:
    """Compute per-section block light (white: R = G = B).

    Emitters (LightSrc > 0) radiate min(15, LightSrc); the value drops by 1
    per Manhattan step and opaque blocks (atten >= 15) block propagation —
    matching real saves (source → 10, air at distance d → 10 - d).

    Args:
        sections: list of {"sec_y", "blocks"}.
        atten: block-type → LightAtten (opaque fallback 15).
        src:   block-type → LightSrc emission (default DEFAULT_LIGHT_SRC).

    Returns:
        sec_y → 2048 packed bytes for sections with any non-zero light,
        None otherwise.
    """
    if atten is None:
        atten = DEFAULT_LIGHT_ATTEN
    if src is None:
        src = DEFAULT_LIGHT_SRC
    blocks = _world_block_grid(sections)
    light = [0] * (16 * 16 * _WORLD_HEIGHT)

    def _idx(x: int, z: int, y: int) -> int:
        return x + z * 16 + y * 256

    def _btype(x: int, z: int, y: int) -> int:
        return blocks[_idx(x, z, y)] & 0xFFF

    from collections import deque

    queue: deque = deque()
    for y in range(_WORLD_HEIGHT):
        for z in range(16):
            for x in range(16):
                s = src.get(_btype(x, z, y), 0)
                if s > 0:
                    v = min(15, s)
                    i = _idx(x, z, y)
                    if v > light[i]:
                        light[i] = v
                        queue.append(i)
    while queue:
        i = queue.popleft()
        x, z, y = i % 16, (i // 16) % 16, i // 256
        L = light[i]
        for nx, nz, ny in ((x - 1, z, y), (x + 1, z, y), (x, z - 1, y), (x, z + 1, y), (x, z, y - 1), (x, z, y + 1)):
            if not (0 <= nx < 16 and 0 <= nz < 16 and 0 <= ny < _WORLD_HEIGHT):
                continue
            if atten.get(_btype(nx, nz, ny), 15) >= 15:
                continue  # opaque: no block light through it
            v = L - 1
            if v <= 0:
                continue
            ni = _idx(nx, nz, ny)
            if v > light[ni]:
                light[ni] = v
                queue.append(ni)

    return _section_nibbles(light, sections)


class LightData158(TypedDict):
    """Result of compute_light_158: per-section light layers + source counts.

    sky/block: sec_y → 2048 packed bytes or None (section without light).
    sources:   sec_y → number of light-emitting blocks (lightFlag low byte).
    """

    sky: Dict[int, Optional[bytes]]
    block: Dict[int, Optional[bytes]]
    sources: Dict[int, int]


def compute_light_158(
    sections: List[dict],
    atten: Optional[Dict[int, int]] = None,
    src: Optional[Dict[int, int]] = None,
) -> LightData158:
    """Compute sky + white block light for a chunk's sections.

    Returns a dict accepted by build_full_chunk_158's ``light`` parameter:
    {"sky": {sec_y: bytes}, "block": {sec_y: bytes}, "sources": {sec_y: n}}
    — ``sources`` holds the per-section light-emitting block count, for
    building realistic section lightFlags (light_flag_for_section_158).
    """
    if src is None:
        src = DEFAULT_LIGHT_SRC
    return {
        "sky": compute_sky_light_158(sections, atten),
        "block": compute_block_light_158(sections, atten, src),
        "sources": _light_source_counts(sections, src),
    }


def _light_source_counts(sections: List[dict], src: Dict[int, int]) -> Dict[int, int]:
    """Per-section count of blocks with LightSrc > 0 (flag low byte, §6)."""
    counts: Dict[int, int] = {}
    for sec in sections:
        sy = int(sec.get("sec_y", 0))
        if not (0 <= sy <= 15):
            continue
        blocks = sec.get("blocks", [0] * BLOCKS_PER_SECTION)
        if isinstance(blocks, (bytes, bytearray)):
            blocks = struct.unpack("<4096H", blocks)
        counts[sy] = sum(1 for b in blocks[:BLOCKS_PER_SECTION] if src.get(int(b) & 0xFFF, 0) > 0)
    return counts


def _world_block_grid(sections: List[dict]) -> List[int]:
    """16×16×256 block-type grid (linear = x + z*16 + y*256). Air = 0."""
    grid = [0] * (16 * 16 * _WORLD_HEIGHT)
    for sec in sections:
        sy = int(sec.get("sec_y", 0))
        if not (0 <= sy <= 15):
            continue
        blocks = sec.get("blocks", [0] * BLOCKS_PER_SECTION)
        if isinstance(blocks, (bytes, bytearray)):
            blocks = struct.unpack("<4096H", blocks)
        base = sy * 4096  # section spans 16 y-levels × 256 cells each
        for i, b in enumerate(blocks[:BLOCKS_PER_SECTION]):
            grid[base + i] = int(b)
    return grid


def _section_nibbles(light: List[int], sections: List[dict]) -> Dict[int, Optional[bytes]]:
    """Slice a 4096-per-section light array into packed 2048-byte vectors.

    Sections with all-zero light map to None (empty element table).
    """
    out: Dict[int, Optional[bytes]] = {}
    for sec in sections:
        sy = int(sec.get("sec_y", 0))
        if not (0 <= sy <= 15):
            continue
        base = sy * 4096  # section spans 16 y-levels × 256 cells each
        if any(light[base + i] for i in range(4096)):
            nib = light[base : base + 4096]
            out[sy] = pack_nibbles_158(nib)
        else:
            out[sy] = None
    return out


# ============================================================================
# Cross-chunk light computation (3x3 chunk grid)
# ============================================================================

# Grid size in blocks: 3 chunks × 16 per axis.
_GRID_SIZE = 48

# Padded-grid geometry: a 1-cell opaque border is added on every side so the
# flood fills can walk flat neighbor deltas with zero bounds checks and no
# index decoding. Border cells carry atten 15 (sky clamps to 0, block light is
# blocked), so light can never escape the inner 48×48×256 region.
_PAD_W = _GRID_SIZE + 2  # 50
_PAD_WW = _PAD_W * _PAD_W  # 2500
_PAD_H = _WORLD_HEIGHT + 2  # 258
_PAD_CELLS = _PAD_W * _PAD_W * _PAD_H
_PAD_DELTAS = (-1, 1, -_PAD_W, _PAD_W, -_PAD_WW, _PAD_WW)  # x±1, z±W, y±W²


def _pack_nibble_row(row: bytearray) -> bytes:
    """Pack a 16-nibble row (values 0..15) into 8 bytes, low nibble first.

    Matches pack_nibbles_158's byte layout for one contiguous 16-cell row:
    byte k = row[2k] | (row[2k + 1] << 4).
    """
    return bytes(
        (
            row[0] | (row[1] << 4),
            row[2] | (row[3] << 4),
            row[4] | (row[5] << 4),
            row[6] | (row[7] << 4),
            row[8] | (row[9] << 4),
            row[10] | (row[11] << 4),
            row[12] | (row[13] << 4),
            row[14] | (row[15] << 4),
        )
    )


def compute_light_grid_158(
    chunks: Mapping[Tuple[int, int], List[dict]],
    atten: Optional[Dict[int, int]] = None,
    src: Optional[Dict[int, int]] = None,
) -> Dict[Tuple[int, int], Dict[str, Dict[int, Optional[bytes]]]]:
    """Compute sky + white block light over a 3x3 chunk grid.

    The center chunk's coordinate is the grid origin; neighbors are placed at
    offsets (-1..1, -1..1). Light (sky flood + block source radiation) spreads
    across chunk borders, so a light source near an edge correctly illuminates
    the adjacent chunk — and breaking it clears both sides.

    Args:
        chunks: {(cx, cz): [{"sec_y", "blocks"}, ...]} — the center chunk plus
            up to 8 neighbors (missing neighbors are treated as air).
        atten: block-type → LightAtten (default built-ins).
        src:   block-type → LightSrc emission (default built-ins).

    Returns:
        {(cx, cz): {"sky": {sec_y: 2048 packed bytes or None},
                    "block": {sec_y: 2048 packed bytes or None}}}
        for every chunk present in *chunks* (center + neighbors provided).
    """
    if atten is None:
        atten = DEFAULT_LIGHT_ATTEN
    if src is None:
        src = DEFAULT_LIGHT_SRC

    # Flat lookup tables for the hot build loop: block types are 12-bit, so a
    # 4096-entry list beats per-block dict.get. atten clamps to [0, 15] (values
    # ≥ 15 behave identically to opaque); src keeps its raw value, emitters are
    # recorded only for s > 0 (matching the old `if s > 0` gate).
    atten_arr = [a if 0 <= a < 15 else (15 if a >= 15 else 0) for a in (atten.get(i, 15) for i in range(4096))]
    src_arr = [src.get(i, 0) for i in range(4096)]

    # Determine the center (minimum cx/cz) so the grid spans a 3x3 area.
    xs = [k[0] for k in chunks]
    zs = [k[1] for k in chunks]
    min_cx, max_cx = min(xs), max(xs)
    min_cz, max_cz = min(zs), max(zs)
    if max_cx - min_cx > 2 or max_cz - min_cz > 2:
        raise ValueError(f"chunk grid too wide: cx {min_cx}..{max_cx}, cz {min_cz}..{max_cz}")

    # ---- build the padded grid: per-cell LightAtten (0..15) + emitter list ----
    # Padded cells default to air (atten 0, src 0); unwritten inner cells (a
    # section absent from *chunks*) are air too, matching the old all-zero grid.
    attn = bytearray(_PAD_CELLS)
    emitters: List[Tuple[int, int]] = []
    for (cx, cz), sections in chunks.items():
        off_x, off_z = cx - min_cx, cz - min_cz
        for sec in sections:
            sy = int(sec.get("sec_y", 0))
            if not (0 <= sy <= 15):
                continue
            blocks = sec.get("blocks", [0] * BLOCKS_PER_SECTION)
            if isinstance(blocks, (bytes, bytearray)):
                blocks = struct.unpack("<4096H", blocks)
            if not any(blocks[:BLOCKS_PER_SECTION]):
                continue  # all-air section: nothing to record
            # Padded base of this section; blocks layout (lx + lz*16 + ly*256)
            # maps to padded strides (1, _PAD_W, _PAD_WW).
            base = (1 + off_x * 16) + (1 + off_z * 16) * _PAD_W + (1 + sy * 16) * _PAD_WW
            for ly in range(16):
                row_base = base + ly * _PAD_WW
                sec_row = ly * 256
                for lz in range(16):
                    cell = row_base + lz * _PAD_W
                    seg = blocks[sec_row + lz * 16 : sec_row + lz * 16 + 16]
                    for j, b in enumerate(seg):
                        bt = int(b) & 0xFFF
                        attn[cell + j] = atten_arr[bt]
                        s = src_arr[bt]
                        if s > 0:
                            emitters.append((cell + j, s if s < 15 else 15))

    # Opaque 1-cell border (x/z/y = 0 and max) — flat-delta BFS stays in-bounds
    # and cannot leak light into the padding.
    for y in range(_PAD_H):
        base = y * _PAD_WW
        for z in range(_PAD_W):
            attn[base + z * _PAD_W] = 15
            attn[base + z * _PAD_W + _PAD_W - 1] = 15
    for y in range(_PAD_H):
        base = y * _PAD_WW
        for z in (0, _PAD_W - 1):
            row = base + z * _PAD_W
            for x in range(_PAD_W):
                attn[row + x] = 15
    for z in range(_PAD_W):
        row = z * _PAD_W
        for x in range(_PAD_W):
            attn[row + x] = 15
            attn[(_PAD_H - 1) * _PAD_WW + row + x] = 15

    # ---- sky light: flood from the top of the grid ----
    from collections import deque

    sky = bytearray(_PAD_CELLS)
    queue: deque = deque()
    qappend = queue.append
    qpop = queue.popleft
    top_base = 256 * _PAD_WW + 1 + _PAD_W  # inner y=255 row
    for z in range(_GRID_SIZE):
        row = top_base + z * _PAD_W
        for x in range(_GRID_SIZE):
            i = row + x
            v = 15 - attn[i]
            if v > sky[i]:
                sky[i] = v
                if v:
                    qappend(i)
    while queue:
        i = qpop()
        lv = sky[i]
        for d in _PAD_DELTAS:
            ni = i + d
            v = lv - attn[ni]
            if v > sky[ni]:
                sky[ni] = v
                if v:
                    qappend(ni)

    # ---- block light: emitters radiate with Manhattan attenuation ----
    block = bytearray(_PAD_CELLS)
    queue.clear()
    for i, s in emitters:
        if s > block[i]:
            block[i] = s
            qappend(i)
    while queue:
        i = qpop()
        lv = block[i]
        for d in _PAD_DELTAS:
            ni = i + d
            if attn[ni] >= 15:
                continue  # opaque: no block light through it
            v = lv - 1
            if v <= 0:
                continue
            if v > block[ni]:
                block[ni] = v
                qappend(ni)

    # ---- slice per chunk ----
    result: Dict[Tuple[int, int], Dict[str, Dict[int, Optional[bytes]]]] = {}
    for (cx, cz), sections in chunks.items():
        off_x, off_z = cx - min_cx, cz - min_cz
        sky_out: Dict[int, Optional[bytes]] = {}
        block_out: Dict[int, Optional[bytes]] = {}
        for sec in sections:
            sy = int(sec.get("sec_y", 0))
            if not (0 <= sy <= 15):
                continue
            base = (1 + off_x * 16) + (1 + off_z * 16) * _PAD_W + (1 + sy * 16) * _PAD_WW
            sky_packed = bytearray(LIGHT_BYTES_PER_SECTION)
            blk_packed = bytearray(LIGHT_BYTES_PER_SECTION)
            sky_has = blk_has = False
            for ly in range(16):
                row_base = base + ly * _PAD_WW
                dst = ly * 128
                for lz in range(16):
                    cell = row_base + lz * _PAD_W
                    off = dst + lz * 8  # 16 nibbles per row → 8 packed bytes
                    srow = sky[cell : cell + 16]
                    if any(srow):
                        sky_has = True
                        sky_packed[off : off + 8] = _pack_nibble_row(srow)
                    brow = block[cell : cell + 16]
                    if any(brow):
                        blk_has = True
                        blk_packed[off : off + 8] = _pack_nibble_row(brow)
            sky_out[sy] = bytes(sky_packed) if sky_has else None
            block_out[sy] = bytes(blk_packed) if blk_has else None
        result[(cx, cz)] = {"sky": sky_out, "block": block_out}
    return result


# ============================================================================
# Block ID encoding / decoding
# ============================================================================
def encode_block_id(block_type: int, subtype: int) -> int:
    """
    Encode block type and subtype into a 16-bit block ID.

    u16 = (subtype << 12) | type ; 12-bit type, 4-bit subtype.

    Raises:
        ValueError: If block_type or subtype out of range.
    """
    if not (0 <= block_type <= 0xFFF):
        raise ValueError(f"block_type {block_type} out of range [0, 0xFFF]")
    if not (0 <= subtype <= 0xF):
        raise ValueError(f"subtype {subtype} out of range [0, 0xF]")
    return (subtype << 12) | block_type


def decode_block_id(u16: int) -> Tuple[int, int]:
    """Decode a 16-bit block ID into (type, subtype)."""
    return u16 & 0xFFF, (u16 >> 12) & 0xF


# ============================================================================
# Palette data model
# ============================================================================


@dataclass
class PaletteEntry158:
    """One palette entry (one distinct block in a section)."""

    block_id: int  # u32 block id
    state_hashes: List[int] = dc_field(default_factory=list)  # per state hash
    state_data: List[int] = dc_field(default_factory=list)  # per state data value


@dataclass
class Section158:
    """Paletted section model: palette + packed index words."""

    sec_y: int
    palette: List[PaletteEntry158]
    data: bytes = b""  # packed 64-bit words (empty when pal<=1)
    light_flag: int = 0  # u16
    _block_count: Optional[int] = None  # cached non-air count (set by build_section_model)

    @property
    def palette_size(self) -> int:
        return len(self.palette)

    @property
    def bits_per_entry(self) -> int:
        return max(4, max(1, self.palette_size - 1).bit_length())

    @property
    def block_count(self) -> int:
        """Number of non-air blocks (block_id != 0)."""
        if self._block_count is None:
            self._block_count = self._compute_block_count()
        return self._block_count

    def _compute_block_count(self) -> int:
        if self.palette_size <= 1 and not self.data:
            return 0 if self.palette[0].block_id == 0 else BLOCKS_PER_SECTION
        counts = [0] * self.palette_size
        bits = self.bits_per_entry
        vpw = 64 // bits
        mask = (1 << bits) - 1
        produced = 0
        for w_off in range(0, len(self.data), 8):
            w = int.from_bytes(self.data[w_off : w_off + 8], "little")
            for i in range(vpw):
                if produced >= BLOCKS_PER_SECTION:
                    break
                counts[(w >> (i * bits)) & mask] += 1
                produced += 1
        return sum(c for i, c in enumerate(counts) if self.palette[i].block_id != 0)


def build_section_model(blocks: List[int], states: Optional[List[int]] = None) -> Section158:
    """
    Build a Section158 model from a flat block list.

    Args:
        blocks: 4096 block ids (list of int, u32). 0 = air.
        states: Optional 4096 per-block data values (0 default).  Distinct
            (block_id, state_data) pairs become distinct palette entries.

    Raises:
        ValueError: If block list length != 4096 or a value is out of u32 range.
    """
    if len(blocks) != BLOCKS_PER_SECTION:
        raise ValueError(f"blocks must have {BLOCKS_PER_SECTION} entries, got {len(blocks)}")
    if states is not None and len(states) != BLOCKS_PER_SECTION:
        raise ValueError(f"states must have {BLOCKS_PER_SECTION} entries, got {len(states)}")

    # Build palette: distinct (block_id, state_data) in first-appearance order.
    # The non-air count is tallied in this same pass so Section158.block_count
    # never has to re-scan the packed data (saves a full 4096-entry pass).
    order: Dict[Tuple[int, int], int] = {}
    entries: List[PaletteEntry158] = []
    index_map: List[int] = [0] * BLOCKS_PER_SECTION
    block_count = 0
    for i, bid in enumerate(blocks):
        bid = int(bid)
        if not (0 <= bid <= 0xFFFFFFFF):
            raise ValueError(f"block id {bid} out of u32 range")
        sd = int(states[i]) if states is not None else 0
        key = (bid, sd)
        pal_idx = order.get(key)
        if pal_idx is None:
            pal_idx = len(entries)
            order[key] = pal_idx
            # air (0) entries carry no state vector; others get a single state
            # with the real block-state hash so the game's FindState resolves it.
            if bid == 0:
                entries.append(PaletteEntry158(block_id=0))
            else:
                entries.append(PaletteEntry158(block_id=bid, state_hashes=[state_hash_for(bid, sd)], state_data=[sd]))
                block_count += 1
        elif bid != 0:
            block_count += 1
        index_map[i] = pal_idx

    # Pack data words. Each word is accumulated as one int and written with a
    # single struct.pack_into — no per-entry slice + int.from_bytes/to_bytes
    # round-trip (~3x faster on typical terrain palettes).
    bits = max(4, max(1, len(entries) - 1).bit_length())
    vpw = 64 // bits
    if len(entries) <= 1:
        data = b""
    else:
        words = (BLOCKS_PER_SECTION + vpw - 1) // vpw
        raw = bytearray(words * 8)
        for w in range(words):
            word = 0
            base = w * vpw
            for j in range(min(vpw, BLOCKS_PER_SECTION - base)):
                word |= index_map[base + j] << (j * bits)
            struct.pack_into("<Q", raw, w * 8, word)
        data = bytes(raw)

    return Section158(sec_y=0, palette=entries, data=data, _block_count=block_count)


# ============================================================================
# Section builder
# ============================================================================


def _mk_table(field_offsets: List[int], inline: bytes) -> bytes:
    """Build a self-contained FlatBuffer table: [soffset][inline][vtable]."""
    buf = bytearray()
    stbl_pos = len(buf)
    buf.extend(b"\x00\x00\x00\x00")  # soffset placeholder
    buf.extend(inline)
    vtbl = _mk_vtable_std(field_offsets, 4 + len(inline))
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, stbl_pos, stbl_pos - vtbl_pos)
    return bytes(buf)


def _mk_state_table(state_hash: int, state_data: int) -> bytes:
    """State table: f0 = hash u32, f2 = data u32."""
    inline = bytearray(8)
    struct.pack_into("<I", inline, 0, state_hash & 0xFFFFFFFF)  # f0 @+4
    struct.pack_into("<I", inline, 4, state_data & 0xFFFFFFFF)  # f2 @+8
    return _mk_table([4, 0, 8], bytes(inline))


def _mk_palette_entry(entry: PaletteEntry158) -> bytes:
    """PaletteEntry table: f0 = block_id u32, f1 = state vector (ALWAYS present).

    f1 is REQUIRED by the game reader (SectionPaletteDecoder @0x1807F9210):
    ``if (*v29)`` dereferences entry.f1 UNCONDITIONALLY (no null check) whenever
    block_id resolves to a valid BlockState — a missing f1 is a guaranteed
    NULL-deref crash (confirmed live game crash @0x1807f9403, R12=0).
    Real 1.58 saves carry f1 on EVERY entry (air = empty vector, len 0).

    Wire layout (table base = t):
      t+4  = block_id (f0)
      t+8  = f1 uoffset = 4  ->  state vector header at t+12 (u32 len),
                                 then uoffset slots, then state tables

    (Fixed 2026-08-09: previously the f1 uoffset was written at t+12 with
    value 0, so the game read an empty vector and the state tables were never
    reached — block variant data was silently lost; air entries had no f1 at
    all, which crashed the game.)
    """
    inline = bytearray(8)
    struct.pack_into("<I", inline, 0, entry.block_id & 0xFFFFFFFF)  # f0 @+4
    # layout: [soffset][inline][state vec header][state vec uoffsets][state tables]
    buf = bytearray()
    buf.extend(inline)
    # state vector header + uoffset placeholders
    vec_pos = len(buf)  # = 8 -> t+12 (vector header)
    buf.extend(struct.pack("<I", len(entry.state_hashes)))
    for _ in entry.state_hashes:
        buf.extend(b"\x00\x00\x00\x00")
    # state tables appended AFTER the vector (forward uoffsets)
    state_positions = []
    for h, d in zip(entry.state_hashes, entry.state_data):
        state_positions.append(len(buf))
        buf.extend(_mk_state_table(h, d))
    for i, st_pos in enumerate(state_positions):
        uoff_abs = vec_pos + 4 + i * 4
        struct.pack_into("<I", buf, uoff_abs, st_pos - uoff_abs)
    # f1 uoffset @ inline[4] (= t+8) -> vector header at buf[8] (= t+12).
    # uoffset is relative to its own position: 8 - 4 = 4.
    struct.pack_into("<I", buf, 4, vec_pos - 4)
    return _mk_table([4, 8], bytes(buf))


def build_section_158(
    sec_y: int,
    blocks: Union[List[int], bytes],
    states: Optional[List[int]] = None,
    light_flag: int = 0,
) -> bytes:
    """
    Build a 1.58 PalettedTable Section table.

    Section table:
      f0 (tag  4) = sec_y u32
      f1 (tag  6) = data vector (packed 64-bit words, u8)
      f2 (tag  8) = palette vector [uoffset → PaletteEntry]
      f3 (tag 10) = blockCount u16
      f4 (tag 12) = lightFlag u16

    Args:
        sec_y:       Section Y (0..15).
        blocks:      4096 block ids (list of int) or 8192 raw bytes (u16[4096]).
        states:      Optional 4096 per-block data values.
        light_flag:  Light flag u16 (default 0).

    Raises:
        ValueError: If sec_y out of range or blocks invalid.
    """
    if not (0 <= sec_y <= 15):
        raise ValueError(f"sec_y {sec_y} out of range [0, 15]")
    if isinstance(blocks, (bytes, bytearray)):
        if len(blocks) != 8192:
            raise ValueError(f"blocks bytes must be 8192, got {len(blocks)}")
        blocks = list(struct.unpack("<4096H", blocks))
    else:
        blocks = list(blocks)
    if light_flag < 0 or light_flag > 0xFFFF:
        raise ValueError(f"light_flag {light_flag} out of u16 range")

    sec_model = build_section_model(blocks, states)
    sec_model.sec_y = sec_y
    sec_model.light_flag = light_flag

    # ---- palette vector header first, then entry tables (forward uoffsets) ----
    entry_buf = bytearray()
    pal_vec_pos = len(entry_buf)
    entry_buf.extend(struct.pack("<I", len(sec_model.palette)))
    for _ in sec_model.palette:
        entry_buf.extend(b"\x00\x00\x00\x00")
    entry_positions: List[int] = []
    for entry in sec_model.palette:
        entry_positions.append(len(entry_buf))
        entry_buf.extend(_mk_palette_entry(entry))
    for i, ep in enumerate(entry_positions):
        uoff_abs = pal_vec_pos + 4 + i * 4
        struct.pack_into("<I", entry_buf, uoff_abs, ep - uoff_abs)

    # ---- data vector (after palette) ----
    data_vec_pos = len(entry_buf)
    entry_buf.extend(_mk_vector(sec_model.data, "B") if sec_model.data else b"\x00\x00\x00\x00")

    # ---- section table inline ----
    # layout: +4 sec_y(u32), +8 blockCount(u16), +10 lightFlag(u16),
    #         +12 data uoffset(u32), +16 palette uoffset(u32) → tsize 20
    sec_inline = bytearray(16)
    struct.pack_into("<I", sec_inline, 0, sec_y & 0xFFFFFFFF)  # f0 @+4
    struct.pack_into("<H", sec_inline, 4, sec_model.block_count)  # f3 @+8
    struct.pack_into("<H", sec_inline, 6, light_flag & 0xFFFF)  # f4 @+10
    entry_buf_abs = 4 + len(sec_inline)  # entry_buf starts here in final buf
    struct.pack_into("<I", sec_inline, 8, entry_buf_abs + data_vec_pos - 12)  # f1 @+12
    struct.pack_into("<I", sec_inline, 12, entry_buf_abs + pal_vec_pos - 16)  # f2 @+16

    sec_fields = [4, 12, 16, 8, 10]  # f0, f1, f2, f3, f4
    # assemble: [soffset][inline][data vec][palette vec + entries]
    buf = bytearray()
    buf.extend(b"\x00\x00\x00\x00")
    buf.extend(sec_inline)
    buf.extend(entry_buf)
    vtbl = _mk_vtable_std(sec_fields, 4 + len(sec_inline))
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, 0, -vtbl_pos)
    return bytes(buf)


# ============================================================================
# Full chunk builder
# ============================================================================


def _mk_legacy_section_entry() -> bytes:
    """Degenerate 9-slot direct-section entry with only f8 = empty postprocess
    vector. Real 1.58 saves carry exactly one such entry in root.f1 — the
    reader unconditionally dereferences root.f1 (0x1807FE60E), so the vector
    (and at least this entry) MUST exist to avoid a NULL-deref crash."""
    buf = bytearray()
    buf.extend(b"\x00\x00\x00\x00")  # soffset
    buf.extend(b"\x00" * 8)  # inline: f8 uoffset @+4
    vec_pos = len(buf)
    buf.extend(b"\x00\x00\x00\x00")  # empty postprocess vector [count=0]
    struct.pack_into("<I", buf, 4, vec_pos - 4)  # f8 @+4 → vec
    fields = [0] * 9
    fields[8] = 4
    vtbl = _mk_vtable_std(fields, 12)
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, 0, -vtbl_pos)
    return bytes(buf)


def build_full_chunk_158(
    sections: List[dict],
    data_version: int = CHUNK_DATA_VERSION_158_0,
    biomes: Optional[bytes] = None,
    light: Optional[Union[str, dict]] = None,
    light_atten: Optional[Dict[int, int]] = None,
    light_src: Optional[Dict[int, int]] = None,
) -> bytes:
    """
    Build a complete 1.58 PalettedTable FlatBuffer chunk.

    Root (16 fields):
      f0 (tag 4)  = biomes u8[256]  (ALWAYS written; reader derefs it when
                    full_sync=1 at 0x1807FDFA7 — default all-0x01 like real saves)
      f1 (tag 6)  = legacy direct-sections vector (ALWAYS written: one degenerate
                    9-slot entry, reader unconditionally derefs at 0x1807FE60E)
      f11 (tag 26) = data_version (u32, default CHUNK_DATA_VERSION_158_0)
      f15 (tag 34) = section container table (7 fields)
           ├─ container.f1 (tag 6) = LIGHT TABLE (4-field, written when light
           │                        is provided/auto-computed; absent → game
           │                        loads empty light layers, chunk is dark)
           └─ container.f2 (tag 8) = sections vector [uoffset → Section]

    Light table (RE/1.58_light_data.md): f0..f3 = sky, block-R, block-G,
    block-B. Each layer = vector of 18 element tables (header + 16 sections
    sec_y 0..15 + spare); a section's element carries f0 = u8[2048] nibble
    data (4096 nibbles) and f1 = u32 flag (1); the header element carries
    flag 2. Sections without light get empty element tables.

    data_version MUST NOT be 0: real 1.58.0 saves carry 0x13A00 and 1.58.2
    saves 0x13A02 (encoding (major<<8)|minor). Passing 0 would not match any
    real save and may route game-side consumers onto a different parse path.

    Args:
        sections: List of dicts with keys:
            sec_y (int): 0..15
            blocks (list[int]|bytes): 4096 block ids
            states (list[int]|None): optional 4096 data values
            light_flag (int): optional u16 (persisted per-section light state,
                default 0. RE/1.58_light_data.md §6: low byte = light-emitting
                block count mod 256, high byte = channel flag (0x0300 sky /
                0x0400 block); set by the light engine on propagation and it
                may lag. Use light_flag_for_section_158() to reproduce the
                common real values; 0 is safe (matches most real sections)).
        data_version: Chunk data version (u32). Default CHUNK_DATA_VERSION_158_0.
        biomes: Optional 256-byte biome data (u8). Default all 0x01 (real value).
        light: Optional lighting:
            None (default) → no light table (game renders the chunk dark).
            "auto" (or True) → compute sky + white block light from the
                section block layout (blockdef LightAtten/LightSrc physics).
            dict → explicit per-section light data, e.g.:
                {"sky":  {0: bytes|list, 1: ...},
                 "block": {0: bytes|list, ...}}        # white block light
                 "block": [{0: r}, {0: g}, {0: b}]}    # RGB channels
                Values are 2048 packed bytes or 4096 nibbles (0..15);
                missing/None sec_y → empty element (no light in that layer).
        light_atten: block-type → LightAtten for "auto" (default built-ins).
        light_src:   block-type → LightSrc for "auto" (default built-ins).

    Returns:
        Complete raw FlatBuffer chunk bytes.

    Raises:
        ValueError: If sections empty or invalid.
    """
    if not sections:
        raise ValueError("sections list must not be empty")
    if len(sections) > 16:
        raise ValueError(f"too many sections: {len(sections)} > 16")
    if data_version == 0:
        raise ValueError(
            "data_version must not be 0: real 1.58 saves carry 0x13A00 (1.58.0) "
            "or 0x13A02 (1.58.2); use CHUNK_DATA_VERSION_158_0/158_2"
        )
    if biomes is None:
        biomes = b"\x01" * 256
    if len(biomes) != 256:
        raise ValueError(f"biomes must be 256 bytes, got {len(biomes)}")

    # ---- light table (container.f1) ----
    light_table: Optional[bytes] = None
    if isinstance(light, str) or light is True:
        if light in (True, "auto"):
            light_data = compute_light_158(sections, light_atten, light_src)
            light_table = build_light_table_158(sky=light_data["sky"], block=[light_data["block"]])
        else:
            raise ValueError(f"light must be 'auto', True, a dict, or None; got {light!r}")
    elif isinstance(light, dict):
        sky = light.get("sky", {})
        block = light.get("block")
        if block is None:
            block = [{}]
        elif isinstance(block, dict):
            block = [block]  # single white channel
        light_table = build_light_table_158(sky=sky, block=block)
    elif light is not None:
        raise ValueError(f"light must be 'auto', True, a dict, or None; got {light!r}")

    # ---- sections vector header first, then section tables (forward uoffsets) ----
    sec_buf = bytearray()
    sec_vec_pos = len(sec_buf)
    sec_buf.extend(struct.pack("<I", len(sections)))
    for _ in sections:
        sec_buf.extend(b"\x00\x00\x00\x00")
    sec_positions: List[int] = []
    for sec in sections:
        sec_positions.append(len(sec_buf))
        sec_buf.extend(
            build_section_158(
                sec_y=sec.get("sec_y", 0),
                blocks=sec.get("blocks", [0] * BLOCKS_PER_SECTION),
                states=sec.get("states"),
                light_flag=sec.get("light_flag", 0),
            )
        )
    for i, sp in enumerate(sec_positions):
        uoff_abs = sec_vec_pos + 4 + i * 4
        struct.pack_into("<I", sec_buf, uoff_abs, sp - uoff_abs)

    # ---- section container table (7 fields, f1 = light table, f2 = sections) ----
    cont_inline = bytearray(20)
    struct.pack_into("<I", cont_inline, 0, 0)  # f0 @+4 (unused)
    struct.pack_into("<I", cont_inline, 4, 0)  # f1 @+8 placeholder (light table)
    struct.pack_into("<I", cont_inline, 8, 0)  # f2 @+12 placeholder (sections)
    struct.pack_into("<I", cont_inline, 12, 0)  # f3 @+16 (unused)
    struct.pack_into("<I", cont_inline, 16, 0)  # f4 @+20 (unused)
    cont_fields = [4, 8, 12, 16, 20, 0, 0]  # 7 slots
    # container body: [soffset][inline][sections vec + tables][light table]
    cont_buf = bytearray()
    cont_buf.extend(b"\x00\x00\x00\x00")
    cont_buf.extend(cont_inline)
    cont_buf.extend(sec_buf)
    # f2 uoffset @+12 (rel table) → sections vector (at 4 + len(inline) in cont_buf)
    f2_abs = 4 + 8  # soffset(4) + f2 offset within inline (8) → @+12
    vec_abs = 4 + len(cont_inline)
    struct.pack_into("<I", cont_buf, f2_abs, vec_abs - f2_abs)
    if light_table is not None:
        light_pos = len(cont_buf)
        cont_buf.extend(light_table)
        f1_abs = 4 + 4  # soffset(4) + f1 offset within inline (4) → @+8
        struct.pack_into("<I", cont_buf, f1_abs, light_pos - f1_abs)
    cont_vtbl = _mk_vtable_std(cont_fields, 4 + len(cont_inline))
    cont_vtbl_pos = len(cont_buf)
    cont_buf.extend(cont_vtbl)
    struct.pack_into("<i", cont_buf, 0, -cont_vtbl_pos)
    container_bytes = bytes(cont_buf)

    # ---- legacy direct-sections vector (root.f1): one degenerate entry ----
    legacy_entry = _mk_legacy_section_entry()
    legacy_buf = bytearray()
    legacy_vec_pos = len(legacy_buf)
    legacy_buf.extend(b"\x01\x00\x00\x00")  # count = 1
    legacy_buf.extend(b"\x00\x00\x00\x00")  # uoffset placeholder
    entry_pos = len(legacy_buf)
    legacy_buf.extend(legacy_entry)
    struct.pack_into("<I", legacy_buf, legacy_vec_pos + 4, entry_pos - (legacy_vec_pos + 4))

    # ---- root table ----
    # inline: +4 f0 biomes uoffset, +8 f1 legacy uoffset, +12 f11 data_version,
    #         +16 f15 container uoffset → tsize = 20
    root_inline = bytearray(16)
    root_fields = [0] * 16
    root_fields[0] = 4
    root_fields[1] = 8
    root_fields[11] = 12
    root_fields[15] = 16
    struct.pack_into("<I", root_inline, 8, data_version & 0xFFFFFFFF)  # f11 @+12

    root_buf = bytearray()
    root_buf.extend(b"\x00\x00\x00\x00")
    root_buf.extend(root_inline)

    # biomes u8[256] (reader reads u8 elements, full_sync path)
    bio_vec_pos = len(root_buf)
    root_buf.extend(_mk_vector(list(biomes), "B"))
    struct.pack_into("<I", root_buf, 4, bio_vec_pos - 4)  # f0 @+4

    # legacy direct-sections vector (root.f1)
    legacy_pos = len(root_buf)
    root_buf.extend(legacy_buf)
    struct.pack_into("<I", root_buf, 8, legacy_pos - 8)  # f1 @+8

    # container table
    cont_pos = len(root_buf)
    root_buf.extend(container_bytes)
    struct.pack_into("<I", root_buf, 4 + 12, cont_pos - (4 + 12))  # f15 @+16

    root_vtbl = _mk_vtable_std(root_fields, 4 + len(root_inline))
    root_vtbl_pos = len(root_buf)
    root_buf.extend(root_vtbl)
    struct.pack_into("<i", root_buf, 0, -root_vtbl_pos)

    # root uoffset at buffer start
    final = bytearray(b"\x00\x00\x00\x00")
    final.extend(root_buf)
    struct.pack_into("<I", final, 0, 4)
    return bytes(final)


# ============================================================================
# Compression
# ============================================================================


# Per-thread ZstdCompressor: creating one per call costs ~6ms vs ~0.2ms for
# the compress itself, BUT a ZstdCompressor instance is NOT thread-safe — the
# chunk parse workers (config.mc.chunk_parse_thread) compress concurrently, so
# a shared singleton corrupts the native ZSTD_CCtx and segfaults the process
# (SIGSEGV in ZSTD_copy16, confirmed via core dump + multi-threaded repro).
_zstd_compressor: "threading.local" = threading.local()


def compress_chunk_158(raw: bytes) -> Tuple[bytes, int]:
    """
    Compress chunk data with zstd (type 3), matching 1.58 format.

    Returns:
        (compressed_bytes, unzip_len) where unzip_len = len(raw) | 0x30000000.

    Raises:
        ImportError: If zstandard library not available.
    """
    import zstandard

    cctx = getattr(_zstd_compressor, "cctx", None)
    if cctx is None:
        cctx = _zstd_compressor.cctx = zstandard.ZstdCompressor()
    compressed = cctx.compress(raw)
    unzip_len = len(raw) | 0x30000000
    return compressed, unzip_len


# ============================================================================
# Self-test
# ============================================================================


def _test():
    """Round-trip self-test using palette semantics."""
    try:  # package import (mn2mc.mini.chunk)
        from .validate_chunk_158 import (
            _read_vtable,
            parse_light_table_158,
            parse_section_158,
        )
    except ImportError:  # standalone script execution
        from validate_chunk_158 import (
            _read_vtable,
            parse_light_table_158,
            parse_section_158,
        )

    print("=== Chunk Builder 1.58 (PalettedTable) Self-Test ===\n")

    # 1. model building
    blocks = [encode_block_id(1, 0)] * 2048 + [encode_block_id(2, 0)] * 1024 + [0] * 1024
    m = build_section_model(blocks)
    assert m.palette_size == 3
    assert m.bits_per_entry == 4
    assert len(m.data) == 2048
    assert m.block_count == 3072
    print("[PASS] build_section_model: pal=3 bits=4 data=2048B block_count=3072")

    # 2. section build + roundtrip
    sec_bytes = build_section_158(sec_y=0, blocks=blocks)
    raw = build_full_chunk_158([{"sec_y": 0, "blocks": blocks}])
    print(f"[PASS] build: chunk {len(raw)}B, section {len(sec_bytes)}B")

    # 3. roundtrip via own reader
    import struct as _s

    root = _s.unpack_from("<I", raw, 0)[0]
    _, _, foffs = _read_vtable(raw, root)
    cont = root + foffs[15] + _s.unpack_from("<I", raw, root + foffs[15])[0]
    _, _, cfoffs = _read_vtable(raw, cont)
    svec = cont + cfoffs[2] + _s.unpack_from("<I", raw, cont + cfoffs[2])[0]
    nsec = _s.unpack_from("<I", raw, svec)[0]
    sec0 = svec + 4 + _s.unpack_from("<I", raw, svec + 4)[0]
    sec = parse_section_158(raw, sec0)
    assert sec["sec_y"] == 0
    assert sec["palette"][0]["block_id"] == 1
    assert sec["block_count"] == 3072
    print(f"[PASS] roundtrip: sec_y={sec['sec_y']} pal={len(sec['palette'])} block_count={sec['block_count']}")

    # 4. light table build + parse
    sky = {0: pack_nibbles_158([15] * LIGHT_NIBBLES_PER_SECTION)}
    raw_light = build_full_chunk_158(
        [{"sec_y": i, "blocks": blocks if i == 0 else [0] * BLOCKS_PER_SECTION} for i in range(16)],
        light={"sky": sky, "block": {0: pack_nibbles_158([5] * LIGHT_NIBBLES_PER_SECTION)}},
    )
    layers = parse_light_table_158(raw_light)
    assert layers is not None and len(layers) == 4
    assert layers[0][0] == b"\xff" * LIGHT_BYTES_PER_SECTION
    assert layers[1][0] == layers[2][0] == layers[3][0] == b"\x55" * LIGHT_BYTES_PER_SECTION
    print(f"[PASS] light table: 4 layers × {LIGHT_ELEMENTS} elements, sky/blk data roundtrips")

    print("\n=== All tests passed ===")


if __name__ == "__main__":
    _test()

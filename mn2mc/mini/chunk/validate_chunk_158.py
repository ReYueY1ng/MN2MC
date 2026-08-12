"""
FlatBuffer chunk validator for Mini World v1.58 PalettedTable format.

Structural + game-logic validation for the REAL 1.58 on-disk chunk format
(verified against actual 1.58.0/1.58.2 saves):

    root.f15 → section container → container.f2 → sections vector
      → section.f0=sec_y, f1=data (packed words), f2=palette, f3=blockCount, f4=lightFlag
        → PaletteEntry.f0=block_id, f1=state vector
          → StateTable.f0=hash, f2=data

Field indexes follow the GUI satellite-tool logic (miniworld_core.ChunkView)
and the 1.58 writer buildChunkFlatBuffer decompile.

References:
  - RE/1.58_world_analysis.md
  - .omo/notepads/chunk-builder-158.md
"""

import struct
from typing import Dict, List, Optional, Tuple

BLOCKS_PER_SECTION = 16 * 16 * 16  # 4096

# ============================================================================
# Vtable reader (self-contained, no external dependency)
# ============================================================================

def _read_vtable(buf: bytes, table_pos: int) -> Tuple[int, int, List[int]]:
    """
    Read vtable from a table, auto-detecting Standard vs Mini format.

    Standard: vtable[0:2]=vsize, vtable[2:4]=tsize
    Mini:     vtable[0:2]=tsize, vtable[2:4]=vsize

    Returns: (vsize, tsize, field_offsets) or raises ValueError.
    """
    if table_pos < 0 or table_pos + 4 > len(buf):
        raise ValueError(f"Table position out of bounds: 0x{table_pos:x}")

    soffset = struct.unpack_from('<i', buf, table_pos)[0]
    vtable_pos = table_pos - soffset

    if vtable_pos < 0 or vtable_pos + 4 > len(buf):
        raise ValueError(
            f"Vtable position out of bounds: 0x{vtable_pos:x} "
            f"(table=0x{table_pos:x}, soffset={soffset})")

    val0 = struct.unpack_from('<H', buf, vtable_pos)[0]
    val2 = struct.unpack_from('<H', buf, vtable_pos + 2)[0]

    def _try(vsize: int, tsize: int) -> Optional[Tuple[int, int, List[int]]]:
        if vsize < 4 or (vsize - 4) % 2 != 0:
            return None
        num_fields = (vsize - 4) // 2
        if vtable_pos + vsize > len(buf):
            return None
        foffs = []
        for i in range(num_fields):
            foffs.append(struct.unpack_from('<H', buf, vtable_pos + 4 + i * 2)[0])
        return vsize, tsize, foffs

    result = _try(val0, val2)
    if result is not None:
        return result
    result = _try(val2, val0)
    if result is not None:
        return result

    raise ValueError(
        f"Cannot parse vtable at 0x{vtable_pos:x}: "
        f"val0=0x{val0:x}, val2=0x{val2:x}")


def _read_uoffset(buf: bytes, pos: int) -> int:
    if pos < 0 or pos + 4 > len(buf):
        raise ValueError(f"uoffset read out of bounds: 0x{pos:x}")
    return pos + struct.unpack_from('<I', buf, pos)[0]


# ============================================================================
# 1.58 palette-semantics readers (mirror GUI ChunkView field indexes)
# ============================================================================
ROOT_SECTION_CONTAINER_FIELD = 15
SECTION_CONTAINER_SECTIONS_FIELD = 2
SECTION_INDEX_FIELD = 0
SECTION_DATA_FIELD = 1
SECTION_PALETTE_FIELD = 2
PALETTE_BLOCK_ID_FIELD = 0
PALETTE_STATE_VECTOR_FIELD = 1
STATE_HASH_FIELD = 0
STATE_DATA_FIELD = 2


def _field_offset(buf: bytes, table_pos: int, field_idx: int) -> Optional[int]:
    """Return absolute field position for *field_idx*, or None if absent."""
    try:
        _, _, foffs = _read_vtable(buf, table_pos)
    except ValueError:
        return None
    if field_idx >= len(foffs) or foffs[field_idx] == 0:
        return None
    return table_pos + foffs[field_idx]


def _read_table_target(buf: bytes, table_pos: int, field_idx: int) -> Optional[int]:
    """Follow a uoffset field to its target table/vector position."""
    pos = _field_offset(buf, table_pos, field_idx)
    if pos is None:
        return None
    try:
        return _read_uoffset(buf, pos)
    except ValueError:
        return None


def parse_section_158(data: bytes, sec_pos: int) -> dict:
    """
    Read a 1.58 PalettedTable section exactly as the game/GUI loads it.

    Returns:
        dict: sec_y, data (bytes, packed words), block_count, light_flag,
              palette: list of {block_id, state_hashes, state_data}.
    """
    sec_y = 0
    pos = _field_offset(data, sec_pos, SECTION_INDEX_FIELD)
    if pos is not None and pos + 4 <= len(data):
        sec_y = struct.unpack_from('<I', data, pos)[0]

    block_count = 0
    pos = _field_offset(data, sec_pos, 3)  # f3 = blockCount u16
    if pos is not None and pos + 2 <= len(data):
        block_count = struct.unpack_from('<H', data, pos)[0]

    light_flag = 0
    pos = _field_offset(data, sec_pos, 4)  # f4 = lightFlag u16
    if pos is not None and pos + 2 <= len(data):
        light_flag = struct.unpack_from('<H', data, pos)[0]

    data_vec = _read_table_target(data, sec_pos, SECTION_DATA_FIELD)
    data_bytes = b""
    if data_vec is not None and data_vec + 4 <= len(data):
        dlen = struct.unpack_from('<I', data, data_vec)[0]
        data_bytes = data[data_vec + 4:data_vec + 4 + dlen]

    pal_vec = _read_table_target(data, sec_pos, SECTION_PALETTE_FIELD)
    palette: List[dict] = []
    if pal_vec is not None and pal_vec + 4 <= len(data):
        n = struct.unpack_from('<I', data, pal_vec)[0]
        for i in range(n):
            uoff_pos = pal_vec + 4 + i * 4
            if uoff_pos + 4 > len(data):
                continue
            entry_tbl = _read_uoffset(data, uoff_pos)
            epos = _field_offset(data, entry_tbl, PALETTE_BLOCK_ID_FIELD)
            block_id = struct.unpack_from('<I', data, epos)[0] if epos else 0
            hashes: List[int] = []
            datas: List[int] = []
            state_vec = _read_table_target(data, entry_tbl, PALETTE_STATE_VECTOR_FIELD)
            if state_vec is not None and state_vec + 4 <= len(data):
                sn = struct.unpack_from('<I', data, state_vec)[0]
                for j in range(sn):
                    suoff = state_vec + 4 + j * 4
                    if suoff + 4 > len(data):
                        break
                    stbl = _read_uoffset(data, suoff)
                    hpos = _field_offset(data, stbl, STATE_HASH_FIELD)
                    dpos = _field_offset(data, stbl, STATE_DATA_FIELD)
                    hashes.append(struct.unpack_from('<I', data, hpos)[0] if hpos else 0)
                    datas.append(struct.unpack_from('<I', data, dpos)[0] if dpos else 0)
            palette.append({"block_id": block_id, "state_hashes": hashes,
                            "state_data": datas})

    return {
        "sec_y": sec_y,
        "data": data_bytes,
        "block_count": block_count,
        "light_flag": light_flag,
        "palette": palette,
    }


def _sections_iter(data: bytes):
    """Yield (root_foffs, container_pos, sec_vec_pos, sec_pos, sec_foffs)."""
    if len(data) < 8:
        return
    root = struct.unpack_from('<I', data, 0)[0]
    try:
        _, _, foffs = _read_vtable(data, root)
    except ValueError:
        return
    if len(foffs) <= ROOT_SECTION_CONTAINER_FIELD or foffs[ROOT_SECTION_CONTAINER_FIELD] == 0:
        return
    try:
        container = _read_uoffset(data, root + foffs[ROOT_SECTION_CONTAINER_FIELD])
        _, _, cfoffs = _read_vtable(data, container)
    except ValueError:
        return
    if len(cfoffs) <= SECTION_CONTAINER_SECTIONS_FIELD or cfoffs[SECTION_CONTAINER_SECTIONS_FIELD] == 0:
        return
    try:
        svec = _read_uoffset(data, container + cfoffs[SECTION_CONTAINER_SECTIONS_FIELD])
        if svec + 4 > len(data):
            return
        nsec = struct.unpack_from('<I', data, svec)[0]
    except ValueError:
        return
    for i in range(nsec):
        if i >= 256:  # hard cap: absurd section counts are corrupt
            break
        uoff_pos = svec + 4 + i * 4
        if uoff_pos + 4 > len(data):
            return
        try:
            sec_pos = _read_uoffset(data, uoff_pos)
        except ValueError:
            return
        yield foffs, container, svec, sec_pos


# ============================================================================
# Light table (container.f1) reader — mirrors the game reader
# (Chunk_LightContainerProcessor @0x1807F9AB0 / Chunk_NibbleArrayCreator
#  @0x1807F9F40; see RE/1.58_light_data.md)
# ============================================================================

LIGHT_TABLE_FIELD = 1     # container.f1 (tag 6) = light table
LIGHT_LAYER_FIELDS = 4    # f0..f3 = sky, block R, block G, block B
LIGHT_ELEMENTS = 18       # [0] header, [1..16] sections sec_y 0..15, [17] spare
LIGHT_HEADER_FLAG = 2
LIGHT_SECTION_FLAG = 1
LIGHT_BYTES_PER_SECTION = 2048


def parse_light_table_158(
    data: bytes, container_pos: Optional[int] = None
) -> Optional[List[Dict[int, Optional[bytes]]]]:
    """Read the container.f1 light table exactly as the game loads it.

    Mirrors Chunk_LightContainerProcessor: the light table is a 4-field
    table (f0..f3 = sky / block R / block G / block B); each field is a
    vector of 18 element tables; element index 1..16 = section sec_y 0..15,
    where a data-bearing element carries f0 = u8[2048] nibble vector
    (4096 nibbles) and f1 = u32 flag (1); empty elements carry nothing.

    Args:
        data: full chunk FlatBuffer bytes.
        container_pos: container table position (auto-resolved if omitted).

    Returns:
        list of 4 dicts {sec_y: 2048 packed bytes or None} (one per layer),
        or None if the container/light table is absent.
    """
    if container_pos is None:
        if len(data) < 8:
            return None
        try:
            root = struct.unpack_from('<I', data, 0)[0]
            _, _, foffs = _read_vtable(data, root)
            if len(foffs) <= ROOT_SECTION_CONTAINER_FIELD or not foffs[ROOT_SECTION_CONTAINER_FIELD]:
                return None
            container_pos = _read_uoffset(data, root + foffs[ROOT_SECTION_CONTAINER_FIELD])
        except ValueError:
            return None
    try:
        _, _, cfoffs = _read_vtable(data, container_pos)
        if len(cfoffs) <= LIGHT_TABLE_FIELD or not cfoffs[LIGHT_TABLE_FIELD]:
            return None
        lt = _read_uoffset(data, container_pos + cfoffs[LIGHT_TABLE_FIELD])
        _, _, lfoffs = _read_vtable(data, lt)
    except ValueError:
        return None

    layers: List[Dict[int, Optional[bytes]]] = []
    for layer in range(LIGHT_LAYER_FIELDS):
        per_section: Dict[int, Optional[bytes]] = {}
        if len(lfoffs) > layer and lfoffs[layer]:
            try:
                vec = _read_uoffset(data, lt + lfoffs[layer])
                n = struct.unpack_from('<I', data, vec)[0]
                if n > LIGHT_ELEMENTS:
                    n = LIGHT_ELEMENTS
                for i in range(1, min(n, LIGHT_ELEMENTS)):  # skip header el[0]
                    el = _read_uoffset(data, vec + 4 + i * 4)
                    f0 = _read_table_target(data, el, 0)
                    if f0 is None:
                        per_section[i - 1] = None
                        continue
                    dlen = struct.unpack_from('<I', data, f0)[0]
                    per_section[i - 1] = data[f0 + 4:f0 + 4 + dlen]
            except (ValueError, struct.error):
                pass
        layers.append(per_section)
    return layers


def light_section_flag_158(
    data: bytes, container_pos: Optional[int] = None
) -> Optional[int]:
    """Read the light-table header flag (element[0].f1, expected 2) — None if
    the chunk has no light table at all."""
    if container_pos is None:
        if len(data) < 8:
            return None
        try:
            root = struct.unpack_from('<I', data, 0)[0]
            _, _, foffs = _read_vtable(data, root)
            if len(foffs) <= ROOT_SECTION_CONTAINER_FIELD or not foffs[ROOT_SECTION_CONTAINER_FIELD]:
                return None
            container_pos = _read_uoffset(data, root + foffs[ROOT_SECTION_CONTAINER_FIELD])
        except ValueError:
            return None
    try:
        _, _, cfoffs = _read_vtable(data, container_pos)
        if len(cfoffs) <= LIGHT_TABLE_FIELD or not cfoffs[LIGHT_TABLE_FIELD]:
            return None
        lt = _read_uoffset(data, container_pos + cfoffs[LIGHT_TABLE_FIELD])
        _, _, lfoffs = _read_vtable(data, lt)
        if not lfoffs or not lfoffs[0]:
            return None
        vec = _read_uoffset(data, lt + lfoffs[0])
        el0 = _read_uoffset(data, vec + 4)
        _, _, efoffs = _read_vtable(data, el0)
        if len(efoffs) <= 1 or not efoffs[1]:
            return None
        return struct.unpack_from('<I', data, el0 + efoffs[1])[0]
    except (ValueError, struct.error):
        return None


# ============================================================================
# Structural validation
# ============================================================================

def validate_structure(data: bytes) -> List[str]:
    """
    Validate PalettedTable FlatBuffer structural integrity.

    Checks: buffer min size, root uoffset, vtable sanity, container table,
    sections vector bounds, per-section table/vtable bounds, data vector
    length sanity, palette vector bounds.

    Returns:
        List of error strings. Empty list means OK.
    """
    errors: List[str] = []

    if len(data) < 8:
        errors.append(f"Buffer too small: {len(data)} bytes (minimum 8)")
        return errors

    root_uoff = struct.unpack_from('<I', data, 0)[0]
    root = root_uoff
    if root + 4 > len(data):
        errors.append(f"Root uoffset 0x{root_uoff:x} beyond buffer (len=0x{len(data):x})")
        return errors

    try:
        _, _, foffs = _read_vtable(data, root)
    except ValueError as e:
        errors.append(f"Root vtable error: {e}")
        return errors

    # root must carry the section container in f15
    if len(foffs) <= ROOT_SECTION_CONTAINER_FIELD or foffs[ROOT_SECTION_CONTAINER_FIELD] == 0:
        errors.append(f"Root missing section container (f{ROOT_SECTION_CONTAINER_FIELD})")
        return errors

    # data_version (f11) must be present and non-zero: real 1.58.0/1.58.2 saves
    # carry 0x13A00 / 0x13A02; 0 would not match any real save.
    if len(foffs) > 11 and foffs[11]:
        dv_pos = root + foffs[11]
        if dv_pos + 4 <= len(data):
            dv = struct.unpack_from('<I', data, dv_pos)[0]
            if dv == 0:
                errors.append(f"Root data_version (f11) is 0 — no real 1.58 save has 0")
    else:
        errors.append("Root missing data_version (f11)")

    # root.f0 (biomes u8[256]) must exist: the reader dereferences it
    # unconditionally on the full_sync path (0x1807FDFA7).
    if len(foffs) <= 0 or foffs[0] == 0:
        errors.append("Root missing biomes (f0) — reader NULL-derefs on full_sync")
    else:
        try:
            bvec = _read_uoffset(data, root + foffs[0])
            if bvec + 4 <= len(data):
                bn = struct.unpack_from('<I', data, bvec)[0]
                if bn != 256:
                    errors.append(f"Root biomes (f0) length {bn}, expected 256")
                if bvec + 4 + bn > len(data):
                    errors.append("Root biomes (f0) extends beyond buffer")
        except ValueError as e:
            errors.append(f"Root biomes (f0) uoffset error: {e}")

    # root.f1 (legacy direct-sections vector) must exist: the reader
    # dereferences it unconditionally (0x1807FE60E).
    if len(foffs) <= 1 or foffs[1] == 0:
        errors.append("Root missing sections (f1) — reader NULL-derefs (crash)")

    try:
        container = _read_uoffset(data, root + foffs[ROOT_SECTION_CONTAINER_FIELD])
        if container + 4 > len(data):
            errors.append(f"Container table beyond buffer: 0x{container:x}")
            return errors
        _, _, cfoffs = _read_vtable(data, container)
    except ValueError as e:
        errors.append(f"Container table error: {e}")
        return errors

    if len(cfoffs) <= SECTION_CONTAINER_SECTIONS_FIELD or cfoffs[SECTION_CONTAINER_SECTIONS_FIELD] == 0:
        errors.append(f"Container missing sections vector (f{SECTION_CONTAINER_SECTIONS_FIELD})")
        return errors

    try:
        svec = _read_uoffset(data, container + cfoffs[SECTION_CONTAINER_SECTIONS_FIELD])
        if svec + 4 > len(data):
            errors.append(f"Sections vector header beyond buffer: 0x{svec:x}")
            return errors
        nsec = struct.unpack_from('<I', data, svec)[0]
    except ValueError as e:
        errors.append(f"Sections vector uoffset error: {e}")
        return errors

    if nsec > 256:
        errors.append(f"Sections count {nsec} > 256")
        return errors

    for si in range(nsec):
        uoff_pos = svec + 4 + si * 4
        if uoff_pos + 4 > len(data):
            errors.append(f"Section[{si}] uoffset beyond buffer")
            continue
        try:
            sec_pos = _read_uoffset(data, uoff_pos)
        except ValueError as e:
            errors.append(f"Section[{si}] uoffset error: {e}")
            continue
        if sec_pos + 4 > len(data):
            errors.append(f"Section[{si}] table beyond buffer: 0x{sec_pos:x}")
            continue
        try:
            _, stsize, sfoffs = _read_vtable(data, sec_pos)
        except ValueError as e:
            errors.append(f"Section[{si}] vtable error: {e}")
            continue
        if stsize < 4:
            errors.append(f"Section[{si}] tsize too small: {stsize}")
        for idx, off in enumerate(sfoffs):
            if off and off >= stsize:
                errors.append(f"Section[{si}] field[{idx}] offset {off} >= tsize {stsize}")
        # data vector sanity (f1): length must be 0 or a sane packed size
        # (2048 B for 4 bits; larger palettes legitimately use more bits)
        dv = _read_table_target(data, sec_pos, SECTION_DATA_FIELD)
        if dv is not None and dv + 4 <= len(data):
            dlen = struct.unpack_from('<I', data, dv)[0]
            if dlen == 0:
                pass
            elif dlen < 4 or dlen % 8 != 0 or dlen > 0x100000:
                errors.append(f"Section[{si}] data length {dlen} implausible")
            if dv + 4 + dlen > len(data):
                errors.append(f"Section[{si}] data extends beyond buffer")

    # container.f1 (light table), when present: 4 layers × 18 element tables;
    # data-bearing elements must carry u8[2048] nibble vectors in-bounds.
    if (len(cfoffs) > LIGHT_TABLE_FIELD and cfoffs[LIGHT_TABLE_FIELD]
            and struct.unpack_from('<I', data, container + cfoffs[LIGHT_TABLE_FIELD])[0] != 0):
        lt = _read_table_target(data, container, LIGHT_TABLE_FIELD)
        if lt is None:
            errors.append("Container light table (f1) uoffset error")
        else:
            try:
                _, _, lfoffs = _read_vtable(data, lt)
                if len(lfoffs) < LIGHT_LAYER_FIELDS or any(
                        not lfoffs[i] for i in range(LIGHT_LAYER_FIELDS)):
                    errors.append("Container light table (f1) missing layer fields")
                for layer in range(min(LIGHT_LAYER_FIELDS, len(lfoffs))):
                    if not lfoffs[layer]:
                        continue
                    lvec = _read_uoffset(data, lt + lfoffs[layer])
                    ln = struct.unpack_from('<I', data, lvec)[0]
                    if ln > LIGHT_ELEMENTS:
                        errors.append(f"Light layer[{layer}] element count {ln} > {LIGHT_ELEMENTS}")
                    for ei in range(min(ln, LIGHT_ELEMENTS)):
                        el = _read_uoffset(data, lvec + 4 + ei * 4)
                        f0 = _read_table_target(data, el, 0)
                        if f0 is None:
                            continue
                        dlen = struct.unpack_from('<I', data, f0)[0]
                        if dlen != 0 and dlen != LIGHT_BYTES_PER_SECTION:
                            errors.append(
                                f"Light layer[{layer}] el[{ei}] data length {dlen}, "
                                f"expected {LIGHT_BYTES_PER_SECTION}")
                        if f0 + 4 + dlen > len(data):
                            errors.append(f"Light layer[{layer}] el[{ei}] data beyond buffer")
            except (ValueError, struct.error) as e:
                errors.append(f"Container light table (f1) parse error: {e}")

    return errors


# ============================================================================
# Game-logic validation
# ============================================================================

def _actual_block_count(sec: dict) -> int:
    """Count non-air blocks from palette + packed data."""
    pal = sec["palette"]
    if not pal:
        return 0
    if len(pal) <= 1 and not sec["data"]:
        return 0 if pal[0]["block_id"] == 0 else BLOCKS_PER_SECTION
    bits = max(4, (len(pal) - 1).bit_length())
    vpw = 64 // bits
    mask = (1 << bits) - 1
    counts = [0] * len(pal)
    produced = 0
    for w_off in range(0, len(sec["data"]), 8):
        w = int.from_bytes(sec["data"][w_off:w_off + 8], "little")
        for i in range(vpw):
            if produced >= BLOCKS_PER_SECTION:
                break
            idx = (w >> (i * bits)) & mask
            if idx >= len(pal):
                return -1  # out-of-range index
            counts[idx] += 1
            produced += 1
    return sum(c for i, c in enumerate(counts) if pal[i]["block_id"] != 0)


def validate_game_logic(data: bytes) -> List[str]:
    """
    Validate game-logic rules on a PalettedTable chunk.

    Checks:
      - sec_y in [0, 15]
      - block_count (f3) equals actual non-air count
      - data length consistent with palette size
      - no palette index out of range
      - block ids are u32 (always true), air = 0

    Returns:
        List of error strings. Empty list means OK.
    """
    errors: List[str] = []
    seen_y: Dict[int, int] = {}

    for foffs, _container, _svec, sec_pos in _sections_iter(data):
        sec = parse_section_158(data, sec_pos)
        sy = sec["sec_y"]
        if sy > 15:
            errors.append(f"Section sec_y={sy} out of range [0,15]")
        if sy in seen_y:
            errors.append(f"Duplicate section sec_y={sy} (slots {seen_y[sy]} and current)")
        seen_y[sy] = sec_pos

        pal = sec["palette"]
        if not pal:
            errors.append(f"Section[{sy}] empty palette")
            continue

        bits = max(4, (len(pal) - 1).bit_length())
        required = 0
        if len(pal) > 1:
            vpw = 64 // bits
            words = (BLOCKS_PER_SECTION + vpw - 1) // vpw
            required = words * 8
        elif not sec["data"] and len(pal) == 1:
            required = 0
        if len(sec["data"]) != required:
            errors.append(
                f"Section[{sy}] data length {len(sec['data'])} != required {required} "
                f"(palette={len(pal)}, bits={bits})")

        actual = _actual_block_count(sec)
        if actual == -1:
            errors.append(f"Section[{sy}] palette index out of range in packed data")
        elif sec["block_count"] != actual:
            errors.append(
                f"Section[{sy}] block_count={sec['block_count']} != actual non-air {actual}")

    return errors


# ============================================================================
# Combined validator
# ============================================================================

def validate_chunk_158(data: bytes) -> List[str]:
    """
    Full validation: structure + game logic.

    Returns:
        Combined list of error strings. Empty = OK.
    """
    errors = validate_structure(data)
    if errors:
        return errors
    return validate_game_logic(data)

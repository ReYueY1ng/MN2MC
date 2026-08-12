"""
Minimal FlatBuffer chunk builder — 精确匹配 ChunkBuffer_LoadFromDecompressed 的
最简单解析路径。

构建的 FlatBuffer 只包含解析器能通过的最少字段:

Root Table (16 fields):
  f[11] = data_version (int32)  ← 设为 0 跳过大量条件分支
  f[15] = world_height (uint16)
  f[1]  = sections (Vector<uoffset to Section>)

Section Table (10 fields):
  f[0] = section_y (uint8)
  f[1] = blocks (Vector<uint16>, 4096 entries)
  f[3] = blocks_ex (Vector<uint32>, 4096 entries)
  f[7] = light_data (Vector<uint8>, 4096 entries)

不包含:
  - biomes (节省 256B + 2×256次 SetBiomeId)
  - block_state_index (节省 4096B)
  - actors / actor_metadata / actor_data
  - physics / game_rules
  - section_structs / postprocess positions

Wire format: Standard FlatBuffer (vsize 在 tsize 前), 匹配游戏 flatBufferVerifier_v2 的期望
"""

import struct
from typing import List, Optional

# ============================================================================
# FlatBuffer 基本构建单元
# ============================================================================

def _mk_vtable_std(field_offsets: List[int], tsize: int) -> bytes:
    """
    Standard FlatBuffer vtable: [vsize:u16][tsize:u16][field0_off:u16]...

    匹配 flatBufferVerifier_v2 的期望格式 (vsize 在前).
    """
    num_fields = len(field_offsets)
    vsize = 4 + num_fields * 2
    parts = [struct.pack('<HH', vsize, tsize)]
    for off in field_offsets:
        parts.append(struct.pack('<H', off))
    return b''.join(parts)


def _mk_vector(values, elem_fmt: str = 'B') -> bytes:
    """FlatBuffer 向量: [count:u32][packed elements...]"""
    vals = list(values)
    n = len(vals)
    return struct.pack(f'<I{n}{elem_fmt}', n, *vals)


# ============================================================================
# Section 构建
# ============================================================================

def build_section(
    section_y: int = 0,
    blocks: Optional[List[int]] = None,
    block_state_index: Optional[bytes] = None,
    blocks_ex: Optional[List[int]] = None,
    light_data: Optional[bytes] = None,
) -> bytes:
    if blocks is None:
        blocks = [0] * 4096
    if len(blocks) != 4096:
        raise ValueError(f"blocks must have 4096 entries, got {len(blocks)}")
    if block_state_index is not None and len(block_state_index) != 4096:
        raise ValueError(f"block_state_index must be 4096 bytes, got {len(block_state_index)}")
    if blocks_ex is not None and len(blocks_ex) != 4096:
        raise ValueError(f"blocks_ex must have 4096 entries, got {len(blocks_ex)}")
    if light_data is not None and len(light_data) != 4096:
        raise ValueError(f"light_data must be 4096 bytes, got {len(light_data)}")

    buf = bytearray()

    OFFSET_F1 = 6
    OFFSET_F2 = 10
    OFFSET_F3 = 14
    OFFSET_F7 = 26

    sec_inline = bytearray()
    sec_inline.extend(struct.pack('<B', section_y & 0xFF))
    sec_inline.extend(b'\x00')
    sec_inline.extend(b'\x00\x00\x00\x00')
    sec_inline.extend(b'\x00\x00\x00\x00')
    sec_inline.extend(b'\x00\x00\x00\x00')
    sec_inline.extend(b'\x00' * 8)
    sec_inline.extend(b'\x00\x00\x00\x00')

    sec_tsize = 4 + len(sec_inline)

    sec_pos = len(buf)
    buf.extend(b'\x00\x00\x00\x00')
    buf.extend(sec_inline)

    blocks_vec_pos = len(buf)
    buf.extend(_mk_vector(blocks, 'H'))
    struct.pack_into('<I', buf, sec_pos + OFFSET_F1,
                     blocks_vec_pos - (sec_pos + OFFSET_F1))

    if block_state_index is not None:
        bsi_vec_pos = len(buf)
        buf.extend(_mk_vector(block_state_index, 'B'))
        struct.pack_into('<I', buf, sec_pos + OFFSET_F2,
                         bsi_vec_pos - (sec_pos + OFFSET_F2))

    if blocks_ex is not None:
        be_vec_pos = len(buf)
        buf.extend(_mk_vector(blocks_ex, 'I'))
        struct.pack_into('<I', buf, sec_pos + OFFSET_F3,
                         be_vec_pos - (sec_pos + OFFSET_F3))

    if light_data is not None:
        ld_vec_pos = len(buf)
        buf.extend(_mk_vector(light_data, 'B'))
        struct.pack_into('<I', buf, sec_pos + OFFSET_F7,
                         ld_vec_pos - (sec_pos + OFFSET_F7))

    vtbl_offsets = [0] * 10
    vtbl_offsets[0] = 4
    vtbl_offsets[1] = OFFSET_F1
    if block_state_index is not None:
        vtbl_offsets[2] = OFFSET_F2
    if blocks_ex is not None:
        vtbl_offsets[3] = OFFSET_F3
    if light_data is not None:
        vtbl_offsets[7] = OFFSET_F7

    vtbl = _mk_vtable_std(vtbl_offsets, sec_tsize)
    vtbl_pos = len(buf)
    buf.extend(vtbl)

    # 填充到 tsize，防止 parser 的解析读到错误字段
    buf.extend(b'\x00' * (sec_tsize - len(vtbl)))

    # 填充 soffset
    struct.pack_into('<i', buf, sec_pos, sec_pos - vtbl_pos)

    return bytes(buf)


# ============================================================================
# Chunk 构建
# ============================================================================

def build_minimal_chunk(
    sections: List[dict],
    data_version: int = 0,
    world_height: int = 256,
) -> bytes:
    """
    构建最小 FlatBuffer chunk，走解析器最简单的路径。

    Root Table (16 字段, tsize=40):
      f[0]  = 跳过 (biomes)
      f[1]  = sections (Vector<uoffset>)
      f[2..10] = 跳过
      f[11] = data_version (int32)   ← = 0 跳过更多解析逻辑
      f[12..14] = 跳过
      f[15] = world_height (uint16)

    不包含 biomes、actors、physics、game_rules，确保解析器走最短路径。

    Args:
        sections: 每个 section dict:
            'section_y'   (int, 默认 0)
            'blocks'      (list[int] 4096, 默认全空气)
            'blocks_ex'   (list[int] 4096, 可选)
            'light_data'  (bytes 4096, 可选)
        data_version: 设为 0 跳过大多数条件分支
        world_height: 世界高度

    Returns:
        FlatBuffer 字节
    """
    if not sections:
        raise ValueError("sections list must not be empty")

    buf = bytearray()

    # ── Root uoffset 占位 ──────────────────────────────────────────────
    buf.extend(b'\x00\x00\x00\x00')

    # ── Root table body (compact, only present fields occupy space) ────
    #
    # 布局 (tsize=38):
    #   +0:  soffset (4B)
    #   +4:  f[1] sections uoffset (4B)
    #   +32: f[11] data_version (int32, 4B)
    #   +36: f[15] world_height (uint16, 2B)
    #
    # 没有 f[0]/biomes. 中间空隙是未使用的 padding.
    #
    # f[11] at table offset instead
    # f[15] is ABSENT in vtable (verifier reads it as uoffset to sub-table)
    ROOT_F1_OFF = 4
    ROOT_F11_OFF = 32

    root_pos = len(buf)
    tsize = ROOT_F11_OFF + 4  # f[11] is int32 (4B)
    buf.extend(b'\x00' * tsize)

    struct.pack_into('<I', buf, root_pos + ROOT_F1_OFF, 0)
    struct.pack_into('<i', buf, root_pos + ROOT_F11_OFF, data_version)
    # f[15] intentionally absent — verifier checks it as a table uoffset

    root_vtbl_offsets = [0] * 16
    root_vtbl_offsets[1] = ROOT_F1_OFF
    root_vtbl_offsets[11] = ROOT_F11_OFF

    root_vtbl = _mk_vtable_std(root_vtbl_offsets, tsize)
    root_vtbl_pos = len(buf)
    buf.extend(root_vtbl)

    # soffset
    struct.pack_into('<i', buf, root_pos, root_pos - root_vtbl_pos)

    # ── Sections vector ────────────────────────────────────────────────
    sec_vec_pos = len(buf)
    buf.extend(struct.pack('<I', len(sections)))
    for _ in sections:
        buf.extend(b'\x00\x00\x00\x00')   # uoffset per section

    f1_abs = root_pos + ROOT_F1_OFF
    struct.pack_into('<I', buf, f1_abs, sec_vec_pos - f1_abs)

    # ── 构建每个 section ────────────────────────────────────────────────
    for i, sec in enumerate(sections):
        sec_bytes = build_section(
            section_y=sec.get('section_y', i),
            blocks=sec.get('blocks'),
            block_state_index=sec.get('block_state_index'),
            blocks_ex=sec.get('blocks_ex'),
            light_data=sec.get('light_data'),
        )
        sec_start = len(buf)
        buf.extend(sec_bytes)

        uoff_abs = sec_vec_pos + 4 + i * 4
        struct.pack_into('<I', buf, uoff_abs, sec_start - uoff_abs)

    # ── Root uoffset ───────────────────────────────────────────────────
    struct.pack_into('<I', buf, 0, root_pos)

    # ── 尾部 padding ───────────────────────────────────────────────────
    buf.extend(b'\x00' * 4)

    return bytes(buf)


# ============================================================================
# 便捷函数: 创建随机测试数据
# ============================================================================

def make_test_section(
    block_ids: Optional[List[int]] = None,
    fill_block_id: int = 0,
    blocks_ex_val: int = 0,
    light_val: int = 0xFF,
    block_state_index_val: int = 0,
) -> dict:
    if block_ids is None:
        block_ids = [fill_block_id] * 4096
    blocks_ex = [blocks_ex_val] * 4096
    light_data = bytes([light_val] * 4096)
    block_state_index = bytes([block_state_index_val] * 4096)
    return {
        'blocks': block_ids,
        'block_state_index': block_state_index,
        'blocks_ex': blocks_ex,
        'light_data': light_data,
    }


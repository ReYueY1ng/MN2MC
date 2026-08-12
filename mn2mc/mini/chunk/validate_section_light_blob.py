"""SectionLightFlatBuffer verifier — 复刻 libsandboxengine @0x1807FC6D0.

PB_SYNC_SECTION_LIGHT_DATA_HC (msgcode 105) 的 LightDataDetail 解压后是一个
4 层光照 FlatBuffer。服务端 `buildSectionLightFlatBuffer` (0x1807FD840) 输出
的结构是【嵌套层表】而非直接向量:

    root table (4 fields, tags 4/6/8/10 = sky / block R / G / B)
      └─ 每个字段 = uoffset → Layer TABLE:
           f0 (tag 4) = uoffset → u8[2048] nibble vector
           f1 (tag 6) = u32 标量 flag (= 1, 服务器存 NibbleArray[0] 的值)

客户端 `loadSectionLightFromBuffer` (0x1807FF780) 解压后调用
`SectionLightFlatBuffer_verify` 做边界校验, 失败即日志
"verify sectionlight buffer failed" (行 2190) 并丢弃该包。

校验器内部函数与游戏一一对应 (libsandboxengine.dll, base 0x180000000):
  _verify_table_start    = sub_1804FB1D0  (flatbuffers VerifyTableStart)
  _verify_offset         = sub_1804C5290  (uoffset 字段边界检查)
  _verify_layer_table    = sub_1807FC5E0  (Layer 表 + 内嵌向量校验)
  verify_section_light_blob = SectionLightFlatBuffer_verify @0x1807FC6D0

已知差异: 游戏 verifier 的 maxDepth=64 / maxTables=1000000 在这里同样生效;
游戏不校验 vtable 的 tsize 字段, 本模块同样不校验 (仅 vsize)。
"""

import struct
from typing import Tuple

MAX_DEPTH = 64
MAX_TABLES = 1000000
MAX_VECTOR_LEN = 0x7FFFFFFF


def _u16(buf: bytes, off: int) -> int:
    return struct.unpack_from("<H", buf, off)[0]


def _u32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]


def _i32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<i", buf, off)[0]


def _vtable(buf: bytes, table: int) -> Tuple[int, int, int]:
    """(vtable_off, vsize, tsize); soffset 有符号, vtable = table - soffset.

    调用前必须保证 0 <= vtable_off <= len(buf) - 2, 否则读取会越界
    (游戏里是指针运算 + 后续边界检查, 无异常)."""
    vt = table - _i32(buf, table)
    return vt, _u16(buf, vt), _u16(buf, vt + 2)


class _State:
    __slots__ = ("depth", "tables")

    def __init__(self) -> None:
        self.depth = 0
        self.tables = 0


def _verify_table_start(buf: bytes, table: int, st: _State) -> bool:
    """sub_1804FB1D0 — flatbuffers VerifyTableStart 的等价校验."""
    size = len(buf)
    if size < 4 or not (0 <= table <= size - 4):
        return False
    st.depth += 1
    st.tables += 1
    if st.depth > MAX_DEPTH or st.tables > MAX_TABLES:
        return False
    vt = table - _i32(buf, table)
    if not (0 <= vt <= size - 2):
        return False
    vsize = _u16(buf, vt)
    if vsize & 1:  # vsize 必须 2 字节对齐 (偶数)
        return False
    if vsize > size or vt > size - vsize:
        return False
    return True


def _verify_offset(buf: bytes, table: int, vtable_byte_off: int) -> bool:
    """sub_1804C5290 — 检查 vtable slot 指向的 uoffset 字段在缓冲区内."""
    size = len(buf)
    vt = table - _i32(buf, table)
    if not (0 <= vt <= size - 2):
        return False
    vsize = _u16(buf, vt)
    if vtable_byte_off < vsize:
        field_off = _u16(buf, vt + vtable_byte_off)
        if field_off:
            f = table + field_off
            if size < 4 or not (0 <= f <= size - 4):
                return False
    return True


def _verify_layer_table(buf: bytes, layer: int, st: _State) -> bool:
    """sub_1807FC5E0 — Layer 表校验: f0 = uoffset → u8 向量 (长度边界),
    f1 (vtable slot byte 6) 为 u32 标量字段."""
    if not _verify_table_start(buf, layer, st):
        return False
    vt, vsize, _tsize = _vtable(buf, layer)
    size = len(buf)
    if vsize > 4:
        f0 = _u16(buf, vt + 4)
        if f0:
            f = layer + f0
            if size < 4 or not (0 <= f <= size - 4):
                return False
        if f0:
            vec = layer + f0 + _u32(buf, layer + f0)  # uoffset 间接目标
            if vec:
                if size < 4 or not (0 <= vec <= size - 4):
                    return False
                length = _u32(buf, vec)
                if length >= MAX_VECTOR_LEN:
                    return False
                if length + 4 > size or vec > size - (length + 4):
                    return False
    if not _verify_offset(buf, layer, 6):
        return False
    st.depth -= 1
    return True


def verify_section_light_blob(buf: bytes) -> Tuple[bool, str]:
    """复刻 SectionLightFlatBuffer_verify @0x1807FC6D0.

    Args:
        buf: 解压后的 105 LightDataDetail FlatBuffer (含根 uoffset 前缀).

    Returns:
        (ok, reason): ok=False 时 reason 说明哪一步校验失败.
    """
    st = _State()
    if len(buf) < 4:
        return False, "buffer < 4 bytes (no root uoffset)"
    root = _u32(buf, 0)
    if not _verify_table_start(buf, root, st):
        return False, f"VerifyTableStart(root @ {root:#x}) failed"

    vt, vsize, _tsize = _vtable(buf, root)
    size = len(buf)

    # f0 (tag 4, sky)
    if vsize > 4:
        f0 = _u16(buf, vt + 4)
        if f0:
            f = root + f0
            if size < 4 or not (0 <= f <= size - 4):
                return False, "root.f0 uoffset field out of bounds"
        if f0:
            layer0 = root + f0 + _u32(buf, root + f0)
            if layer0:
                if not _verify_layer_table(buf, layer0, st):
                    return False, "root.f0 (sky) layer table verify failed"

    # f1 (tag 6, block R)
    if not _verify_offset(buf, root, 6):
        return False, "root.f1 uoffset field out of bounds"
    if vsize > 6:
        f1 = _u16(buf, vt + 6)
        if f1:
            layer1 = root + f1 + _u32(buf, root + f1)
            if layer1:
                if not _verify_layer_table(buf, layer1, st):
                    return False, "root.f1 (block R) layer table verify failed"

    # f2 (tag 8, block G)
    if not _verify_offset(buf, root, 8):
        return False, "root.f2 uoffset field out of bounds"
    if vsize > 8:
        f2 = _u16(buf, vt + 8)
        if f2:
            layer2 = root + f2 + _u32(buf, root + f2)
            if layer2:
                if not _verify_layer_table(buf, layer2, st):
                    return False, "root.f2 (block G) layer table verify failed"

    # f3 (tag 10, block B)
    if not _verify_offset(buf, root, 10):
        return False, "root.f3 uoffset field out of bounds"
    if vsize > 10:
        f3 = _u16(buf, vt + 10)
        if f3:
            layer3 = root + f3 + _u32(buf, root + f3)
            if layer3:
                if not _verify_layer_table(buf, layer3, st):
                    return False, "root.f3 (block B) layer table verify failed"

    return True, "ok"


# ============================================================================
# 参考构建: 正确的嵌套 Layer 表结构 (供测试与外部项目对照修复)
# ============================================================================

def build_section_light_blob_correct(sky, block):
    """正确 105 blob 构建 (嵌套 Layer 表) — 正式实现见 section_light_blob_builder.

    旧实现把 root.fN 直接指向 u8 向量, 被游戏 verify 拒绝
    ("verify sectionlight buffer failed", 行 2190)。"""
    try:  # package import (mn2mc.mini.chunk)
        from .section_light_blob_builder import build_section_light_blob
    except ImportError:  # standalone script execution
        from section_light_blob_builder import build_section_light_blob
    return build_section_light_blob(sky, block)


def build_section_light_blob_old_style(sky: bytes, block: bytes) -> bytes:
    """复现旧错误结构 (root.fN → 直接 u8 向量) 供测试/对照 — 应被 verify 拒绝."""
    if len(sky) != 2048 or len(block) != 2048:
        raise ValueError("sky/block must be 2048 bytes each")

    def _mk_vtable(field_offsets: list, tsize: int) -> bytes:
        vsize = 4 + len(field_offsets) * 2
        return struct.pack("<HH", vsize, tsize) + b"".join(
            struct.pack("<H", o) for o in field_offsets)

    buf = bytearray()
    table_pos = len(buf)
    buf.extend(b"\x00\x00\x00\x00")
    buf.extend(b"\x00" * 16)
    pos = []
    for layer in (sky, block, block, block):
        pos.append(len(buf))
        buf.extend(struct.pack("<I", len(layer)) + layer)
    for i, p in enumerate(pos):
        uoff_abs = table_pos + 4 + i * 4
        struct.pack_into("<I", buf, uoff_abs, p - uoff_abs)
    vtbl = _mk_vtable([4, 8, 12, 16], 20)
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, table_pos, table_pos - vtbl_pos)
    final = bytearray(b"\x00\x00\x00\x00")
    final.extend(buf)
    struct.pack_into("<I", final, 0, 4)
    return bytes(final)

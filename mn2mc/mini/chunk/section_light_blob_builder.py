"""PB_SYNC_SECTION_LIGHT_DATA_HC (msgcode 105) LightDataDetail 构建器.

生成与真实服务器 `buildSectionLightFlatBuffer` (libsandboxengine @0x1807FD840)
字节级一致的结构 (RE/1.58_sync_section_light_data.md §3.1/§4.5):

    root table (4 fields, tags 4/6/8/10 = sky / block R / G / B)
      └─ 每字段 = uoffset → Layer 表:
           f0 (tag 4) = uoffset → u8[2048] nibble 向量 (low nibble first)
           f1 (tag 6) = u32 标量 flag (真实值 1; 服务器在值为 0 时省略该字段)
      Layer 表 vtable: 08 00 0c 00 04 00 08 00  (vsize 8 / tsize 12)

服务器行为 (sub_1807FC2F0 / sub_1807F8510):
  - 空层 (NibbleArray 为空) → layer uoffset = 0 → 根字段省略
  - flag 值 = NibbleArray[0] (离线元素 f1), 为 0 时 Layer 表不写 f1

构建结果可直接用 `validate_section_light_blob.verify_section_light_blob`
复验 (本模块构建时已自动自检)。
"""

import struct
from typing import List, Optional, Sequence, Tuple, Union

NIBBLES_PER_SECTION = 16 * 16 * 16  # 4096
BYTES_PER_SECTION = NIBBLES_PER_SECTION // 2  # 2048
LAYER_FLAG = 1  # 真实存档/服务器使用的 Layer 表 f1 值

# 游戏读端 NibbleArray 构造器 (libminiblock EIS2335...) 固定拷贝 0x800 字节;
# 向量长度必须恰好 2048, 否则会读到向量外的数据.
_VECTOR_LEN = BYTES_PER_SECTION


def _mk_vtable(field_offsets: Sequence[int], tsize: int) -> bytes:
    """[vsize:u16][tsize:u16][field_off:u16]...  vsize 在前 (匹配游戏格式)."""
    vsize = 4 + len(field_offsets) * 2
    return struct.pack("<HH", vsize, tsize) + b"".join(struct.pack("<H", o) for o in field_offsets)


def pack_nibbles(values: Union[bytes, Sequence[int]]) -> bytes:
    """4096 nibble (0..15) → 2048 字节, 偶数下标在低 nibble (NibbleArray 布局).

    与游戏 NibbleArray 一致: 第 2i 个值在字节 i 低 4 位, 第 2i+1 个在高 4 位.
    2048 字节输入直接透传.
    """
    if isinstance(values, (bytes, bytearray)):
        if len(values) != BYTES_PER_SECTION:
            raise ValueError(f"packed light must be {BYTES_PER_SECTION} bytes, got {len(values)}")
        return bytes(values)
    if len(values) != NIBBLES_PER_SECTION:
        raise ValueError(f"light nibbles must have {NIBBLES_PER_SECTION} entries, got {len(values)}")
    out = bytearray(BYTES_PER_SECTION)
    for i, v in enumerate(values):
        v = int(v)
        if not (0 <= v <= 0xF):
            raise ValueError(f"nibble {v} out of range [0, 15]")
        if i % 2 == 0:
            out[i // 2] |= v
        else:
            out[i // 2] |= v << 4
    return bytes(out)


def _layer_is_empty(data: bytes) -> bool:
    return not data or data.count(0) == len(data)


def _mk_layer_table(data: bytes, flag: int) -> bytes:
    """构建一个 Layer 表: [soffset][f0 uoff @+4][f1 u32 @+8][u8[2048] vec][vtable].

    flag=0 时省略 f1 (服务器行为: 只保留一个 2-slot 表, vtable 08 00 08 00 04 00).
    """
    buf = bytearray()
    buf.extend(b"\x00\x00\x00\x00")  # soffset
    buf.extend(b"\x00\x00\x00\x00")  # f0 uoffset @+4
    if flag:
        buf.extend(struct.pack("<I", flag))  # f1 u32 @+8
    vec_pos = len(buf)
    buf.extend(struct.pack("<I", len(data)))
    buf.extend(data)
    struct.pack_into("<I", buf, 4, vec_pos - 4)  # f0 uoffset → vector
    tsize = 4 + (8 if flag else 4)  # soffset + inline
    vtbl = _mk_vtable([4, 8] if flag else [4], tsize)
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, 0, -vtbl_pos)
    return bytes(buf)


def build_section_light_blob(
    sky: Union[bytes, Sequence[int], None],
    block: Union[bytes, Sequence[int], Sequence[Union[bytes, Sequence[int], None]], None],
    layer_flag: int = LAYER_FLAG,
    omit_empty: bool = True,
) -> bytes:
    """构建 105 LightDataDetail FlatBuffer (单 section 4 层光照).

    Args:
        sky:   天光层 — 2048 packed bytes / 4096 nibble (0..15), 或 None
            (该层不写入 → 客户端保留旧值)。
        block: 方块光层 — bytes / nibble 序列 → 白光照, R=G=B 复制三份
            (真实存档行为); 3 元素序列 (每元素为 bytes / nibble 序列 / None)
            → R/G/B, None 元素 = 对应通道省略; None → 全部 3 个方块光通道省略。
        layer_flag: Layer 表 f1 u32 值 (默认 1, 与真实数据一致; 0 → 省略 f1 字段).
        omit_empty: 全零层省略根字段 (默认 True, 服务器行为);
            False → 写全零 2048 字节向量 (用于向客户端清除旧光照).
            None 层不受此参数影响 (恒省略)。

    Returns:
        完整 FlatBuffer blob (含根 uoffset 前缀), 已通过游戏等价 verify 自检.

    Raises:
        ValueError: 输入长度/取值非法, 或自检失败.
    """
    try:  # package import (mn2mc.mini.chunk)
        from .validate_section_light_blob import verify_section_light_blob
    except ImportError:  # standalone script execution
        from validate_section_light_blob import verify_section_light_blob

    def _norm(layer: object) -> Optional[bytes]:
        if layer is None:
            return None
        if isinstance(layer, (bytes, bytearray)):
            return pack_nibbles(layer)
        if isinstance(layer, (list, tuple)):
            return pack_nibbles(layer)  # type: ignore[arg-type]
        raise TypeError(f"unexpected layer type: {type(layer)}")

    if block is None:
        block_layers = [None, None, None]
    elif isinstance(block, (bytes, bytearray)):
        block_layers = [_norm(block)] * 3
    elif block and isinstance(block[0], (bytes, bytearray, list, tuple, type(None))):
        if len(block) != 3:
            raise ValueError(f"RGB block light needs 3 layers, got {len(block)}")
        block_layers = [_norm(b) for b in block]  # type: ignore[arg-type]
    else:
        block_layers = [_norm(block)] * 3  # type: ignore[arg-type]

    sky_b = _norm(sky)
    layer_data = [(sky_b, 0)] + [
        (data, i + 1) for i, data in enumerate(block_layers)
    ]  # (data, field index): sky=0, R/G/B=1/2/3
    layers: List[Tuple[bytes, int]] = []
    for data, field_idx in layer_data:
        if data is None:
            continue  # 未变化层 → 根字段省略 (客户端保留旧值)
        if omit_empty and _layer_is_empty(data):
            continue  # 空层 → 根字段省略 (uoffset 保持 0)
        layers.append((_mk_layer_table(data, layer_flag), field_idx))

    buf = bytearray()
    table_pos = len(buf)
    buf.extend(b"\x00\x00\x00\x00")  # soffset
    buf.extend(b"\x00" * 16)  # f0..f3 uoffset @+4..+16
    positions = []
    for table, _i in layers:
        positions.append((len(buf), _i))
        buf.extend(table)
    for p, i in positions:
        field_abs = table_pos + 4 + i * 4
        struct.pack_into("<I", buf, field_abs, p - field_abs)

    vtbl = _mk_vtable([4, 8, 12, 16], 20)
    vtbl_pos = len(buf)
    buf.extend(vtbl)
    struct.pack_into("<i", buf, table_pos, table_pos - vtbl_pos)

    final = bytearray(b"\x00\x00\x00\x00")
    final.extend(buf)
    struct.pack_into("<I", final, 0, 4)
    blob = bytes(final)

    ok, reason = verify_section_light_blob(blob)
    if not ok:
        raise ValueError(f"built blob failed game-equivalent verify: {reason}")
    return blob


def compress_section_light_blob(blob: bytes) -> Tuple[bytes, int]:
    """zstd 压缩 + UnzipLen 组装 (type 3, 匹配 105 消息).

    Returns:
        (compressed, unzip_len); unzip_len = len(blob) | 0x30000000.
    """
    import zstandard

    compressed = zstandard.ZstdCompressor().compress(blob)
    return compressed, len(blob) | 0x30000000

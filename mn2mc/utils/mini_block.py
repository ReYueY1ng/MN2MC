import javascript


def encode_block(id_, x, y, z):
    """
    编码方块信息。
    格式：大端 [id:12][x:4][z:4][y:8] 打包成 28 位整数。
    若 id >= 4096，则 id_mod = id % 4096，商 = id // 4096 单独返回。
    返回：(encoded, quotient)
    """
    if not (0 <= x <= 15 and 0 <= y <= 255 and 0 <= z <= 15):
        raise ValueError("坐标超出范围")
    max_id = 4096
    quotient = id_ // max_id
    id_mod = id_ % max_id
    encoded = (id_mod << 16) | (x << 12) | (z << 8) | y
    return encoded, quotient


def decode_block(encoded, quotient=0):
    """
    解码，需提供商（若原始 id 未超过 4095，商为 0）。
    返回：(original_id, x, y, z)
    """
    id_mod = (encoded >> 16) & 0xFFF  # 高 12 位
    x = (encoded >> 12) & 0xF
    z = (encoded >> 8) & 0xF
    y = encoded & 0xFF
    original_id = quotient * 4096 + id_mod
    return original_id, x, y, z


javascript.eval_js("""
class MiniBlock {
    constructor() {}

    encodeBlock(id, x, y, z) {
        if (!(0 <= x && x <= 15)) throw new RangeError('x must be 0..15');
        if (!(0 <= y && y <= 255)) throw new RangeError('y must be 0..255');
        if (!(0 <= z && z <= 15)) throw new RangeError('z must be 0..15');

        const MAX_ID_BITS = 4096;  // 2^12
        const quotient = Math.floor(id / MAX_ID_BITS);
        const idMod = id % MAX_ID_BITS;

        const encoded = (idMod << 16) | (x << 12) | (z << 8) | y;
        return { encoded, quotient };
    }

    decodeBlock(encoded, quotient = 0) {
        const idMod = (encoded >> 16) & 0xFFF;   // 高12位
        const x     = (encoded >> 12) & 0xF;     // 次4位
        const z     = (encoded >> 8)  & 0xF;     // 中间4位
        const y     = encoded & 0xFF;            // 低8位

        const id = quotient * 4096 + idMod;
        return { id, x, y, z };
    }
}

global.MiniBlock = new MiniBlock()
""")

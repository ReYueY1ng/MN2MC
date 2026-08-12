from typing import Optional

from mn2mc.data.loader import load_block_face

# "方块ID": "可否被变向（0没有方向无法变向，1四向，2六、八向，3特殊处理）"
mini_block_face = load_block_face()

def get_block_face(blockid: int, properties: Optional[dict]):
    if not properties:
        return 0

    face = mini_block_face.get(blockid, 0)
    match face:
        case 0:
            return 0
        case 1: # 四向
            mc_face = properties['facing'] if 'facing' in properties else 'none'
            match mc_face:
                case 'north':
                    return 2
                case 'south':
                    return 3
                case 'east':
                    return 0
                case 'west':
                    return 1
                case _:
                    return 0
        case 2: # 六八向
            mc_face = properties['facing'] if 'facing' in properties else 'none'
            match mc_face:
                case 'east':
                    return 0
                case 'west':
                    return 1
                case 'north':
                    return 2
                case 'south':
                    return 3
                case 'down':
                    return 4
                case 'up':
                    return 5
                case _:
                    return 0
        case _:
            return 0

from mn2mc.data.loader import load_blocks

# MC id: Mini id
mc_to_mini_mapping: dict[int, int] = load_blocks()
mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items()}


def mc_to_mini(id: int) -> int:
    if id in mc_to_mini_mapping:
        return mc_to_mini_mapping[id]
    else:
        return 470  # 问号方块


def mini_to_mc(id: int) -> int:
    if id in mini_to_mc_mapping:
        return mini_to_mc_mapping[id]
    else:
        return 9  # 土块

from mn2mc.data.loader import load_mobs

mc_to_mini_mapping = load_mobs()
mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items()}


def mc_to_mini(id: int) -> int:
    if id in mc_to_mini_mapping:
        return mc_to_mini_mapping[id]
    else:
        return 3284  # 猪


def mini_to_mc(id: int) -> int:
    if id in mini_to_mc_mapping:
        return mini_to_mc_mapping[id]
    else:
        return 100  # 猪

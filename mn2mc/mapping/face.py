mc_to_mini_mapping = {
    0: 4,  # -Y
    1: 5,  # +Y
    2: 2,  # -Z
    3: 3,  # +Z
    4: 1,  # -X
    5: 0,  # +X
}

mini_to_mc_mapping = {v: k for k, v in mc_to_mini_mapping.items()}


def mc_to_mini(id: int) -> int:
    return mc_to_mini_mapping[id]


def mini_to_mc(id: int) -> int:
    return mini_to_mc_mapping[id]

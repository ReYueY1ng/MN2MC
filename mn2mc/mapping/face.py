from mn2mc.mapping.base import BidirectionalMapping

_mapping = BidirectionalMapping(
    {
        0: 4,  # -Y
        1: 5,  # +Y
        2: 2,  # -Z
        3: 3,  # +Z
        4: 1,  # -X
        5: 0,  # +X
    },
)
mc_to_mini_mapping: dict[int, int] = _mapping.forward
mini_to_mc_mapping: dict[int, int] = _mapping.reverse


def mc_to_mini(id: int) -> int:
    return _mapping.mc_to_mini(id)


def mini_to_mc(id: int) -> int:
    return _mapping.mini_to_mc(id)

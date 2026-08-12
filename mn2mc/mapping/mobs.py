from mn2mc.data.loader import load_mobs
from mn2mc.mapping.base import BidirectionalMapping

_mapping = BidirectionalMapping(load_mobs(), mc_default=3284, mini_default=100)
mc_to_mini_mapping: dict[int, int] = _mapping.forward
mini_to_mc_mapping: dict[int, int] = _mapping.reverse


def mc_to_mini(id: int) -> int:
    return _mapping.mc_to_mini(id)


def mini_to_mc(id: int) -> int:
    return _mapping.mini_to_mc(id)

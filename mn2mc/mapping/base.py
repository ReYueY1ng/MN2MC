"""Shared bidirectional ID mapping base for mapping submodules."""

from typing import cast

_MISSING: object = object()


class BidirectionalMapping:
    """Bidirectional int-keyed ID mapping with optional fallback defaults."""

    __slots__ = ("forward", "reverse", "_mc_default", "_mini_default")

    def __init__(
        self,
        forward: dict[int, int],
        mc_default: int | object = _MISSING,
        mini_default: int | object = _MISSING,
    ) -> None:
        self.forward: dict[int, int] = forward
        self.reverse: dict[int, int] = {v: k for k, v in forward.items()}
        self._mc_default = mc_default
        self._mini_default = mini_default

    def mc_to_mini(self, key: int) -> int:
        if self._mc_default is _MISSING:
            return self.forward[key]
        return self.forward.get(key, cast(int, self._mc_default))

    def mini_to_mc(self, key: int) -> int:
        if self._mini_default is _MISSING:
            return self.reverse[key]
        return self.reverse.get(key, cast(int, self._mini_default))

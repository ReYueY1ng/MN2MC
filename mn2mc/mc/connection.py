"""MC protocol connection and event binding."""
from __future__ import annotations

import threading
from typing import TYPE_CHECKING

import mn2mc.config as config
from mn2mc.constants import DIMENSION_OVERWORLD
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f

if TYPE_CHECKING:
    import javascript  # noqa: F401

    from mn2mc.mini.player import MiniPlayer


class MCConnection:
    """Manages MC protocol connection, positional state, and event binding."""

    def __init__(self, client, miniplayer: MiniPlayer) -> None:
        self.client = client
        self.miniplayer = miniplayer
        self.state = "handshaking"
        self._connected = False
        self.running = threading.Event()
        self.running.set()
        self.position = Vector3f()
        self.angle = Angle(0, 0)
        self.on_ground = True
        self._dimension = DIMENSION_OVERWORLD
        self.registry = None  # prismarine-registry instance, set by caller

    # ------------------------------------------------------------------
    # Protocol helpers (forward to underlying JS client)
    # ------------------------------------------------------------------

    def send(self, name: str, message: dict, ignorestate: bool = False) -> None:
        if self.state == "play" or ignorestate:
            self.client.write(name, message)

    def chat(self, content: str, ignorestate: bool = False) -> None:
        if self.state == "play" or ignorestate:
            self.client.chat(content)

    def end(self) -> None:
        self.client.end()

    # ------------------------------------------------------------------
    # Dimension property with world-height side-effects
    # ------------------------------------------------------------------

    @property
    def dimension(self) -> int:
        return self._dimension

    @dimension.setter
    def dimension(self, value: int) -> None:
        self._dimension = value
        self._apply_dimension_height(value)

    def _apply_dimension_height(self, dimid: int) -> None:
        """Update world height when dimension changes."""
        if not hasattr(self.registry, "dimensionsById") or self.registry.dimensionsById is None:
            return
        dimdata = self.registry.dimensionsById[dimid]
        if dimdata is None:
            return
        from loguru import logger

        logger.debug(f"({self.miniplayer.name}) dimension change {dimdata}")
        self.set_world_miny(dimdata.minY)
        self.set_world_height(dimdata.height)

    @staticmethod
    def set_world_miny(miny: int) -> None:
        if not config.mc.use_new_chunk_parser:
            import mn2mc.mc.packetevents.chunk.map_chunk as map_chunk

            map_chunk.miny = miny

    @staticmethod
    def set_world_height(height: int) -> None:
        if not config.mc.use_new_chunk_parser:
            import mn2mc.mc.packetevents.chunk.map_chunk as map_chunk

            map_chunk.worldheight = height

    # ------------------------------------------------------------------
    # Reset state (used when reconnecting / setting up connection)
    # ------------------------------------------------------------------

    def reset_state(self) -> None:
        """Reset mutable positional/connection state to defaults."""
        self.position = Vector3f()
        self.angle = Angle(0, 0)
        self._dimension = DIMENSION_OVERWORLD

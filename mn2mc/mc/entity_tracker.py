"""Entity and player tracking for MC protocol."""
from __future__ import annotations

from typing import TYPE_CHECKING

from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.entity import MCEntity

if TYPE_CHECKING:
    from mn2mc.mc.client import MCClient


class MCEntityTracker:
    """Tracks MC entities and players."""

    def __init__(self) -> None:
        self.entities: dict[int, MCEntity] = {}
        self.players: dict = {}
        self.entityid: int = 0
        self.add_player_count: int = 0

    def reset(self) -> None:
        """Reset all tracked entity/player state."""
        self.entities.clear()
        self.players.clear()
        self.entityid = 0
        self.add_player_count = 0

    def resolve_objid(self, client: MCClient, entityid: int) -> int | None:
        """Resolve MC entity ID to Mini World objid.

        Returns:
            int: The corresponding Mini World objid
            None: Entity is unknown/untracked (caller should ignore)
        """
        if entityid == self.entityid:
            return client.miniplayer.uin
        if entityid not in self.entities:
            return None
        for player_data in self.players.values():
            if player_data.get("entityid") == entityid:
                return player_data["uin"]
        return MINI_OBJ_ID_BASE + entityid

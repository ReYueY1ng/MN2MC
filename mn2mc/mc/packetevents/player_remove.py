"""Handle MC player_remove and clean up tracked Mini World player state."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Remove disconnected players from the client's tracked player map.

    Deletes entries by UUID so stale mappings are not reused.
    """
    for uuid in jsondata["players"]:
        if uuid in client.players:
            del client.players[uuid]


add_event("player_remove", on_recv)

"""Handle Mini World close container packets and translate to MC close_window."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Close the current container window on the MC client.

    Resets tracked window state and sends close_window to the server.
    """
    player.mcclient.send("close_window", {"windowId": player.mcclient.window_id})
    player.mcclient.window_id = 0
    player.mcclient.inventory_type = "inventory"


add_event(proto.common.ePBMsgCode.PB_CLOSE_CONTAINER_CH, on_recv)

"""Handle Mini World backpack grid discard and translate to MC window_click."""

from __future__ import annotations

import mn2mc.mapping.slotid as slotid_mapping
import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Drop or discard an item from a backpack grid.

    Grid 7000 is treated as the cursor slot and mapped to slot -999.
    Other grids are translated via slotid mapping.
    """
    discard = proto.ch.PB_BackPackGridDiscardCH()
    discard.ParseFromString(mcp.data)

    if discard.GridId == 7000:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": -999,
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
    else:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, discard.GridId
                ),
                "mode": 4,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )


add_event(proto.common.ePBMsgCode.PB_BACKPACK_GRID_DISCARD_CH, on_recv)

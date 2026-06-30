"""Handle Mini World backpack grid swap and translate to MC window_click."""

from __future__ import annotations

import mn2mc.mapping.slotid as slotid_mapping
import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Swap items between two backpack grids.

    Skips grid 978 (unknown special case) and maps Mini World slot IDs
    to MC window_click parameters.
    """
    swap = proto.ch.PB_BackPackGridSwapCH()
    swap.ParseFromString(mcp.data)

    if swap.ToGridId == 978:  # ???
        return

    if swap.FromGridId == 7000:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, swap.ToGridId
                ),
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
    else:
        if (999 > swap.ToGridId > 1010) or (999 > swap.FromGridId > 1010):
            player.mcclient.send(
                "window_click",
                {
                    "windowId": player.mcclient.window_id,
                    "stateId": player.mcclient.container_sequence,
                    "slot": slotid_mapping.mini_to_mc(
                        player.mcclient.inventory_type,
                        swap.ToGridId
                        if 999 > swap.ToGridId > 1010
                        else swap.FromGridId,
                    ),
                    "mode": 2,
                    "mouseButton": swap.FromGridId - 1000
                    if 999 > swap.FromGridId > 1010
                    else swap.ToGridId - 1000,
                    "changedSlots": [],
                },
            )


add_event(proto.common.ePBMsgCode.PB_BACKPACK_GRID_SWAP_CH, on_recv)

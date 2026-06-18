"""Handle Mini World backpack move item and translate to MC window_click."""

from __future__ import annotations

import mn2mc.mini.proto as proto
import mn2mc.mapping.slotid as slotid_mapping
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Move an item between inventory slots.

    Handles cursor-to-grid, grid-to-cursor, and shift-click (grid-to-grid)
    moves by mapping slot IDs and sending the appropriate window_click mode.
    """
    move = proto.ch.PB_BackPackMoveItemCH()
    move.ParseFromString(mcp.data)

    if move.ToIndex == 7000:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, move.FromIndex
                ),
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
    elif move.FromIndex == 7000:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, move.ToIndex
                ),
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
        # 服务端不会发设置鼠标物品包
        player.send_packet(
            proto.common.ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
            proto.hc.PB_BackPackGridUpdateHC(
                ItemInfo=[
                    proto.common.PB_ItemData(
                        Index=7000,
                        ItemID=0,
                    )
                ]
            ).SerializeToString(),
        )
    else:  # shift + lmc
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, move.FromIndex
                ),
                "mode": 1,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )


add_event(proto.common.ePBMsgCode.PB_BACKPACK_MOVEITEM_CH, on_recv)

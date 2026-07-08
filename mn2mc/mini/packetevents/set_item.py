"""Handle Mini World backpack set item and translate to MC creative slot updates."""

from __future__ import annotations

from javascript import require

import mn2mc.config as config
import mn2mc.mapping.items as item_mapping
import mn2mc.mapping.slotid as slotid_mapping
import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer

prismarine_item = require("prismarine-item")(config.mc.version)


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Set an item in a specific backpack grid.

    Converts Mini World item IDs to MC IDs and sends set_creative_slot
    plus a backpack grid update back to the client.
    """
    setitem = proto.ch.PB_BackPackSetItemCH()
    setitem.ParseFromString(mcp.data)
    item = prismarine_item(item_mapping.mini_to_mc(setitem.ItemId), setitem.Num)
    itemdata = prismarine_item.toNotch(item)

    if setitem.ToIndex == 7000:
        player.mcclient.send(
            "set_creative_slot",
            {"slot": 1, "item": itemdata},
        )
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": 1,
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
    else:
        player.mcclient.send(
            "set_creative_slot",
            {
                "slot": slotid_mapping.mini_to_mc("inventory", setitem.ToIndex),
                "item": itemdata,
            },
        )
        player.send_packet(
            proto.common.ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
            proto.hc.PB_BackPackGridUpdateHC(
                ItemInfo=[
                    proto.common.PB_ItemData(
                        Index=setitem.ToIndex,
                        ItemID=setitem.ItemId
                        if setitem.ItemId in item_mapping.mini_to_mc_mapping
                        else 101,
                        Num=setitem.Num,
                    )
                ]
            ).SerializeToString(),
        )


add_event(proto.common.ePBMsgCode.PB_BACKPACK_SETITEM_CH, on_recv)

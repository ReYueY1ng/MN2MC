"""Handle MC set_cursor_item and update Mini World cursor slot state."""

from __future__ import annotations

from javascript import require

import mn2mc.config as config
import mn2mc.mapping.items as item_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_ItemData, ePBMsgCode
from mn2mc.mini.proto.hc import PB_BackPackGridUpdateHC

prismarine_item = require("prismarine-item")(config.mc.version)


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Translate MC cursor item into Mini World grid update (index 7000).

    Maps MC item IDs to Mini World IDs and preserves count/durability.
    """
    itemdata = jsondata["contents"]
    item = prismarine_item.fromNotch(itemdata)

    if itemdata["itemCount"] == 0:
        client.miniplayer.send_packet(
            ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
            PB_BackPackGridUpdateHC(
                ItemInfo=[
                    PB_ItemData(
                        Index=7000,
                        ItemID=0,
                    )
                ]
            ).SerializeToString(),
        )
    else:
        client.miniplayer.send_packet(
            ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
            PB_BackPackGridUpdateHC(
                ItemInfo=[
                    PB_ItemData(
                        Index=7000,
                        ItemID=item_mapping.mc_to_mini(item.type),
                        Num=item.count,
                        Durable=item.durabilityUsed,
                    )
                ]
            ).SerializeToString(),
        )


add_event("set_cursor_item", on_recv)

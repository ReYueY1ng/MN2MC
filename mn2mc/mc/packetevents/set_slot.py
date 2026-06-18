"""Handle MC set_slot and synchronize window slot contents to Mini World."""

from __future__ import annotations

import mn2mc.config as config
import mn2mc.mapping.slotid as slotid_mapping
import mn2mc.mapping.items as item_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode, PB_ItemData
from mn2mc.mini.proto.hc import PB_BackPackGridUpdateHC
from javascript import require

prismarine_item = require("prismarine-item")(config.mc["version"])


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Update a single window slot in Mini World.

    Tracks container sequence for the active window and converts MC item
    data to Mini World PB_ItemData.
    """
    slot = jsondata["slot"]
    window = jsondata["windowId"]
    # client.window_id = window
    if client.window_id == window:  # 防止副手刷新替换掉顺序id
        client.container_sequence = jsondata["stateId"]
    itemdata = jsondata["item"]
    item = prismarine_item.fromNotch(itemdata)

    if window == 0:
        inventory_type = "inventory"
    else:
        inventory_type = client.inventory_type

    if itemdata["itemCount"] == 0:
        client.miniplayer.send_packet(
            ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
            PB_BackPackGridUpdateHC(
                ItemInfo=[
                    PB_ItemData(
                        Index=slotid_mapping.mc_to_mini(inventory_type, slot),
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
                        Index=slotid_mapping.mc_to_mini(inventory_type, slot),
                        ItemID=item_mapping.mc_to_mini(item.type),
                        Num=item.count,
                        Durable=item.durabilityUsed,
                    )
                ]
            ).SerializeToString(),
        )


add_event("set_slot", on_recv)

"""Handle MC window_items and synchronize full container contents to Mini World."""

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
    """Translate a full window_items payload into Mini World backpack updates.

    Maps MC slot IDs and item IDs, including the carried cursor item.
    """
    window = jsondata["windowId"]
    client.container_sequence = jsondata["stateId"]
    items = jsondata["items"]

    itemlist: list[PB_ItemData] = []

    if window == 0:
        inventory_type = "inventory"
    else:
        inventory_type = client.inventory_type

    for k, content in enumerate(items):
        if content["itemCount"] == 0:
            itemlist.append(
                PB_ItemData(
                    Index=slotid_mapping.mc_to_mini(inventory_type, k),
                    ItemID=0,
                )
            )
            continue
        item = prismarine_item.fromNotch(content)
        itemlist.append(
            PB_ItemData(
                Index=slotid_mapping.mc_to_mini(inventory_type, k),
                ItemID=item_mapping.mc_to_mini(item.type),
                Num=item.count,
                Durable=item.durabilityUsed,
            )
        )

    if jsondata["carriedItem"]["itemCount"] == 0:
        itemlist.append(
            PB_ItemData(
                Index=7000,
                ItemID=0,
            )
        )
    else:
        item = prismarine_item.fromNotch(jsondata["carriedItem"])
        itemlist.append(
            PB_ItemData(
                Index=7000,
                ItemID=item_mapping.mc_to_mini(item.type),
                Num=item.count,
                Durable=item.durabilityUsed,
            )
        )

    client.miniplayer.send_packet(
        ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
        PB_BackPackGridUpdateHC(ItemInfo=itemlist).SerializeToString(),
    )


add_event("window_items", on_recv)

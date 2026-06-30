"""Handle MC window_items and synchronize full container contents to Mini World."""

from __future__ import annotations

from javascript import require

import mn2mc.config as config
import mn2mc.mapping.items as item_mapping
import mn2mc.mapping.slotid as slotid_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_ItemData, ePBMsgCode
from mn2mc.mini.proto.hc import PB_BackPackGridUpdateHC

prismarine_item = require("prismarine-item")(config.mc["version"])


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
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

    data = PB_BackPackGridUpdateHC(ItemInfo=itemlist).SerializeToString()

    if window != 0 and getattr(client, "_open_pending", False):
        with client._lock:
            if len(client._pending_item_packets) < client.MAX_PENDING_ITEMS:
                client._pending_item_packets.append(
                    (ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC, data)
                )
        return

    client.miniplayer.send_packet(
        ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC, data
    )


add_event("window_items", on_recv)

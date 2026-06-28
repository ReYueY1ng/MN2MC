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


def _make_backpack_update(
    inventory_type: str | int, slot: int, itemdata: dict, item
) -> bytes:
    if itemdata["itemCount"] == 0:
        return PB_BackPackGridUpdateHC(
            ItemInfo=[
                PB_ItemData(
                    Index=slotid_mapping.mc_to_mini(inventory_type, slot),
                    ItemID=0,
                )
            ]
        ).SerializeToString()
    return PB_BackPackGridUpdateHC(
        ItemInfo=[
            PB_ItemData(
                Index=slotid_mapping.mc_to_mini(inventory_type, slot),
                ItemID=item_mapping.mc_to_mini(item.type),
                Num=item.count,
                Durable=item.durabilityUsed,
            )
        ]
    ).SerializeToString()


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    slot = jsondata["slot"]
    window = jsondata["windowId"]
    if client.window_id == window:
        client.container_sequence = jsondata["stateId"]
    itemdata = jsondata["item"]
    item = prismarine_item.fromNotch(itemdata)

    if window == 0:
        inventory_type = "inventory"
    else:
        inventory_type = client.inventory_type

    data = _make_backpack_update(inventory_type, slot, itemdata, item)

    if window != 0 and getattr(client, "_open_pending", False):
        client._pending_item_packets.append(
            (ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC, data)
        )
        return

    client.miniplayer.send_packet(
        ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC, data
    )


add_event("set_slot", on_recv)

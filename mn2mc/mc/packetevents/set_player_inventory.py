import mn2mc.config as config
import mn2mc.mapping.slotid as slotid_mapping
import mn2mc.mapping.items as item_mapping
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode, PB_ItemData
from mn2mc.mini.proto.hc import PB_BackPackGridUpdateHC
from javascript import require

prismarine_item = require("prismarine-item")(config.mc["version"])


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    slot = jsondata["slotId"]
    content = jsondata["content"]
    item = prismarine_item.fromNotch(content)

    client.miniplayer.send_packet(
        ePBMsgCode.PB_BACKPACK_GRID_UPDATE_HC,
        PB_BackPackGridUpdateHC(
            ItemInfo=[
                PB_ItemData(
                    Index=slotid_mapping.mc_to_mini("direct", slot),
                    ItemID=item_mapping.mc_to_mini(item.type),
                    Num=item.count,
                    Durable=item.durabilityUsed,
                )
            ]
        ).SerializeToString(),
    )


add_event("set_player_inventory", on_recv)

"""Handle MC update_health and synchronize health/food to Mini World."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayerAttrChangeHC

# MC health 0-20 → Mini HP 0-100 (default MaxHP = 100)
# MC food 0-20 → Mini FoodLevel 0-100
HP_MULTIPLIER = 5.0
FOOD_MULTIPLIER = 5.0


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Translate MC health/food updates to Mini World attribute packets.

    MC sends health (f32, 0-20), food (varint, 0-20), foodSaturation (f32).
    Mini World uses HP on a 0-100 scale and FoodLevel on a 0-100 scale.
    """
    mc_health = jsondata["health"]
    mc_food = jsondata["food"]

    # Scale conversion
    mini_hp = mc_health * HP_MULTIPLIER
    mini_food = int(mc_food * FOOD_MULTIPLIER)

    attr_change = PB_PlayerAttrChangeHC(
        HP=float(mini_hp),
        FoodLevel=mini_food,
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYER_ATTR_CHANGE_HC, attr_change)


add_event("update_health", on_recv)

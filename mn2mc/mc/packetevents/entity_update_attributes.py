"""Handle MC entity_update_attributes — sync attribute changes to Mini World.

Only the player's own entity (client.entityid) is currently mapped.
General entity attribute updates are logged and skipped.
"""

from __future__ import annotations

from typing import Any

from loguru import logger

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import (
    PB_ActorAttrChangeHC,
    PB_ActorAttrSpeedChangeHC,
    PB_PlayerAttrChangeHC,
)

# minecraft-data 的 entity_update_attributes 属性 ID→名称 映射表（1.21.6/1.21.8/1.21.9/1.21.11）
# 漏了 mining_efficiency / movement_efficiency / oxygen_bonus / sneaking_speed 四个属性，
# 导致 ID>=20 的属性名整体偏移 -4（如真实 movement_speed 的 ID 22 被解析成 generic.scale）。
# 这里把上游解析出的错名还原为真实属性名，后续 match 全部按真实名。
_ATTRIBUTE_OFFSET_MAP = {
    "generic.movement_speed": "mining_efficiency",
    "generic.safe_fall_distance": "movement_efficiency",
    "generic.scale": "generic.movement_speed",
    "zombie.spawn_reinforcements": "oxygen_bonus",
    "generic.step_height": "generic.safe_fall_distance",
    "submerged_mining_speed": "generic.scale",
    "sweeping_damage_ratio": "sneaking_speed",
    "tempt_range": "zombie.spawn_reinforcements",
    "water_movement_efficiency": "generic.step_height",
    "waypoint_transmit_range": "submerged_mining_speed",
    "waypoint_receive_range": "sweeping_damage_ratio",
}

# 上游映射表只到 ID 30，真实注册表 ID 31~34（tempt_range / water_movement_efficiency /
# waypoint_transmit_range / waypoint_receive_range）会以原始数字到达（如 key=32），一并还原为真名。
_NUMERIC_ATTRIBUTE_MAP = {
    31: "tempt_range",
    32: "water_movement_efficiency",
    33: "waypoint_transmit_range",
    34: "waypoint_receive_range",
}


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Map MC entity attributes to Mini World attribute/speed change packets."""
    entityid = jsondata["entityId"]
    objid = client.resolve_objid(entityid)
    if objid is None:
        return

    #logger.debug(jsondata)
    properties: list[dict] = jsondata.get("properties", [])

    # Only handle the player's own entity
    if entityid != client.entityid:
        #logger.debug(
        #    "entity_update_attributes: skipping non-player entity {} ({} properties)",
        #    entityid,
        #    len(properties),
        #)
        return

    attr_kwargs: dict[str, Any] = {}
    speed_kwargs: dict[str, float] = {}
    send_attr = False
    send_speed = False

    for prop in properties:
        key = prop.get("key", "")
        value = prop.get("value", 0.0)
        if isinstance(key, int):
            key = _NUMERIC_ATTRIBUTE_MAP.get(key, key)
        elif isinstance(key, str):
            key = _ATTRIBUTE_OFFSET_MAP.get(key, key)

        match key:
            case "generic.armor":
                attr_kwargs["Armor"] = value
                send_attr = True
            case "generic.armor_toughness":
                pass
            case "generic.max_health":
                attr_kwargs["MaxHP"] = value * 5.0
                send_attr = True
            case "generic.attack_damage":
                pass
            case "generic.movement_speed":
                speed_kwargs["WalkSpeed"] = value * 100.0
                send_speed = True
            case "generic.flying_speed":
                speed_kwargs["FlySpeed"] = value
                send_speed = True
            case "sneaking_speed":
                speed_kwargs["SneakSpeed"] = value
                send_speed = True
            case "generic.jump_strength":
                speed_kwargs["JumpSpeed"] = value
                send_speed = True
            case "generic.scale":
                # 真实体型，Mini World 暂无对应映射
                pass
            case "generic.gravity":
                pass
            case _:
                logger.debug(
                    "entity_update_attributes: unhandled key '{}' = {}",
                    key,
                    value,
                )

    if objid == client.miniplayer.uin:
        if send_attr:
            msg = PB_PlayerAttrChangeHC(**attr_kwargs).SerializeToString()
            client.miniplayer.send_packet(ePBMsgCode.PB_PLAYER_ATTR_CHANGE_HC, msg)
            #logger.debug(
            #    "player {} attrs changed: {}",
            #    objid,
            #    [k for k in attr_kwargs if k != "ObjID"],
            #)

        if send_speed:
            msg = PB_ActorAttrSpeedChangeHC(**speed_kwargs).SerializeToString()
            client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_SPEED_CHANGE_HC, msg)
            #logger.debug(
            #    "entity {} speed attrs changed: {}",
            #    entityid,
            #    list(speed_kwargs.keys()),
            #)
    elif send_attr:
        attr_kwargs["ObjID"] = objid
        msg = PB_ActorAttrChangeHC(**attr_kwargs).SerializeToString()
        client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_ATTR_CHANGE_HC, msg)
        #logger.debug(
        #    "entity {} attrs changed: {}",
        #    entityid,
        #    [k for k in attr_kwargs if k != "ObjID"],
        #)


add_event("entity_update_attributes", on_recv)

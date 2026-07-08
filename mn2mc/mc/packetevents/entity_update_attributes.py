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


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Map MC entity attributes to Mini World attribute/speed change packets."""
    entityid = jsondata["entityId"]
    objid = client.resolve_objid(entityid)
    if objid is None:
        return

    logger.debug(jsondata)
    properties: list[dict] = jsondata.get("properties", [])

    # Only handle the player's own entity
    if entityid != client.entityid:
        logger.debug(
            "entity_update_attributes: skipping non-player entity {} ({} properties)",
            entityid,
            len(properties),
        )
        return

    attr_kwargs: dict[str, Any] = {}
    speed_kwargs: dict[str, float] = {}
    send_attr = False
    send_speed = False

    for prop in properties:
        key = prop.get("key", "")
        value = prop.get("value", 0.0)

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
                pass
            case "generic.flying_speed":
                speed_kwargs["FlySpeed"] = value
                send_speed = True
            case "geneirc.sweeping_damage_ratio": # sneak speed
                speed_kwargs["SneakSpeed"] = value
                send_speed = True
            case "generic.jump_strength":
                speed_kwargs["JumpSpeed"] = value
                send_speed = True
            case "generic.scale": # 实际上应该是 walk speed
                #attr_kwargs["Scale"] = PB_Vector3f(X=value, Y=value, Z=value)
                #send_attr = True
                speed_kwargs["WalkSpeed"] = value * 100.0
                send_speed = True
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
            logger.debug(
                "player {} attrs changed: {}",
                objid,
                [k for k in attr_kwargs if k != "ObjID"],
            )

        if send_speed:
            msg = PB_ActorAttrSpeedChangeHC(**speed_kwargs).SerializeToString()
            client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_SPEED_CHANGE_HC, msg)
            logger.debug(
                "entity {} speed attrs changed: {}",
                entityid,
                list(speed_kwargs.keys()),
            )
    elif send_attr:
        attr_kwargs["ObjID"] = objid
        msg = PB_ActorAttrChangeHC(**attr_kwargs).SerializeToString()
        client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_ATTR_CHANGE_HC, msg)
        logger.debug(
            "entity {} attrs changed: {}",
            entityid,
            [k for k in attr_kwargs if k != "ObjID"],
        )


add_event("entity_update_attributes", on_recv)

"""Handle MC remove_entity_effect — remove status effects from Mini World entities."""

from __future__ import annotations

from loguru import logger

from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import PB_ActorBuff, ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorBuffChangeHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Remove a status effect from an entity."""
    entityid = jsondata.get("entityId", 0)
    if entityid == client.entityid:
        objid = client.miniplayer.uin
    elif entityid in client.entities:
        for _, player in client.players.items():
            if "entityid" in player and player["entityid"] == entityid:
                objid = player["uin"]
                break
        else:
            objid = MINI_OBJ_ID_BASE + entityid
    else:
        return
    effect_id = jsondata.get("effectId", 0)

    entity = client.entities.get(entityid)
    if entity is None:
        logger.warning("remove_entity_effect: unknown entity {}", entityid)
        return

    removed = entity.buffs.pop(effect_id, None)
    if removed is None:
        logger.debug(
            "effect {} not active on entity {}, skipping removal",
            effect_id, entityid,
        )
        return

    # Rebuild buff list without the removed effect
    remaining = [
        PB_ActorBuff(
            BuffID=data["buff_id"],
            BuffLV=data["amplifier"],
            Ticks=data["duration"],
            BuffInstanceId=data["instance_id"],
            RandomValue=0,
        )
        for data in entity.buffs.values()
    ]

    msg = PB_ActorBuffChangeHC(
        ObjID=objid,
        Buffs=remaining,
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_ACTOR_BUFF_CHANGE_HC, msg)

    logger.debug(
        "effect {} removed from entity {}, {} buff(s) remain",
        effect_id, objid, len(remaining),
    )


add_event("remove_entity_effect", on_recv)

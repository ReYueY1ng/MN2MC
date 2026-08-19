from __future__ import annotations

from javascript import require

import mn2mc.mapping.items as item_mapping
from mn2mc.config import config
from mn2mc.constants import MINI_OBJ_ID_BASE, VELOCITY_SCALING
from mn2mc.mc.client import MCClient
from mn2mc.mc.entity import entitytypes
from mn2mc.mc.entity_metadata import ItemEntityMetadata, PlayerMetadata
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import (
    PB_ActorAttInfo,
    PB_ActorCommon,
    PB_ActorItem,
    ePBMsgCode,
)
from mn2mc.mini.proto.hc import PB_ActorLeaveAOIHC, PB_ActorMotionHC, PB_GeneralEnterAOIHC, PB_PlayerAttrChangeHC
from mn2mc.utils.vector import Vector3

prismarine_item = require("prismarine-item")(config.mc.version)


def _handle_item(client: MCClient, entityid: int, metadata: ItemEntityMetadata):
    if not metadata.has("item"):
        return

    mini_obj_id = MINI_OBJ_ID_BASE + entityid
    item = prismarine_item.fromNotch(metadata.item)

    entity = client.entities[entityid]

    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
        PB_ActorLeaveAOIHC(ObjID=mini_obj_id).SerializeToString(),
    )

    client.miniplayer.send_packet(
        ePBMsgCode.PB_GENERAL_ENTER_AOI_HC,
        PB_GeneralEnterAOIHC(
            ObjID=mini_obj_id,
            MapId=0,
            ActorItem=PB_ActorItem(
                basedata=PB_ActorCommon(
                    wid=mini_obj_id,
                    pos=entity.pos.convert().to_vec3().to_mini(),
                    motion=Vector3().to_mini(),
                    yaw=entity.angle.to_mini_yaw_int32(),
                    pitch=entity.angle.to_mini_pitch_int32(),
                    flags=0,
                    falldist=0,
                    liveticks=0,
                    attinfo=PB_ActorAttInfo(),
                    masterobjid=0,
                    cancollide=True,
                ),
                itemid=item_mapping.mc_to_mini(item.type),
                num=item.count,
                durable=-1,
            ),
        ).SerializeToString(),
    )

    motion = entity.motion.convert()
    motion.x *= VELOCITY_SCALING
    motion.y *= VELOCITY_SCALING
    motion.z *= VELOCITY_SCALING
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_MOTION_HC,
        PB_ActorMotionHC(
            ObjID=mini_obj_id,
            x=motion.x,
            y=motion.y,
            z=motion.z,
            isChangePos=False,
        ).SerializeToString(),
    )


def _handle_self(client: MCClient, _entityid: int, metadata: PlayerMetadata):
    attr_change = PB_PlayerAttrChangeHC()
    if metadata.has("air_ticks"):
        attr_change.Oxygen = metadata.air_ticks / 30
    client.miniplayer.send_packet(ePBMsgCode.PB_PLAYER_ATTR_CHANGE_HC, attr_change.SerializeToString())


def on_recv(client: MCClient, jsondata: dict, _metadata: dict):
    entityid = jsondata["entityId"]
    if entityid not in client.entities:
        return

    raw = jsondata["metadata"]

    if client.entities[entityid].type == entitytypes["item"]:
        _handle_item(client, entityid, ItemEntityMetadata.from_protocol(raw))
    elif entityid == client.entityid:
        _handle_self(client, entityid, PlayerMetadata.from_protocol(raw))


add_event("entity_metadata", on_recv)

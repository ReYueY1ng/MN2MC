from __future__ import annotations

from loguru import logger

import mn2mc.mapping.items as item_mapping
from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.entity import entitytypes
from mn2mc.mini.proto.common import (
    PB_ActorCommon,
    ePBMsgCode,
    PB_ActorAttInfo, PB_ActorItem,
)
from mn2mc.mini.proto.hc import PB_GeneralEnterAOIHC, PB_ActorLeaveAOIHC, PB_ActorMotionHC
from mn2mc.config import config
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f, Vector3
from javascript import require
prismarine_item = require("prismarine-item")(config.mc["version"])

def _handle_item(client: MCClient, entityid: int, metadata):
    """Send AOI enter packet for a item entity."""
    mini_obj_id = MINI_OBJ_ID_BASE + entityid
    item = prismarine_item.fromNotch(metadata[8]['value'])

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
                durable=-1
            )
        ).SerializeToString(),
    )
    
    motion = entity.motion.convert()
    motion.x /= 100
    motion.y /= 100
    motion.z /= 100
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

def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    entityid = jsondata['entityId']
    entitymetadata = {}
    if entityid not in client.entities:
        return
    for meta in jsondata['metadata']:
        entitymetadata[meta['key']] = meta
    if client.entities[entityid].type == entitytypes['item']:
        _handle_item(client, entityid, entitymetadata)

add_event('entity_metadata', on_recv)
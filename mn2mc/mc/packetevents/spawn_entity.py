"""Handle MC spawn_entity and create Mini World AOI entries."""

from __future__ import annotations

from loguru import logger

import mn2mc.mapping.mobs as mob_mapping
import mn2mc.mini.skin as skin
from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.entity import MCEntity
from mn2mc.mini.proto.common import (
    PB_ActorCommon,
    PB_ActorInfo,
    PB_ActorMob,
    PB_ActorRoleInfo,
    PB_BodyDir,
    PB_PlayerInfo,
    PB_Pos,
    PB_RoleData,
    PB_RoleInfo,
    ePBMsgCode,
    PB_ActorAttInfo, PB_ActorItem,
)
from mn2mc.mini.proto.hc import (
    PB_ActorEnterAOIHC,
    PB_GeneralEnterAOIHC,
    PB_ActorLeaveAOIHC,
)
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f, Vector3

# Entity types that should be ignored (not spawned in Mini World).
_IGNORED_ENTITY_TYPES = frozenset({
    5,   # armor stand
    131, # text display
    93,  # painting
    73,  # item frame
    72,  # item display
    49,  # experience orb
    15,  # block display
    60,  # glow item frame
})

# MC entity type ID for players.
_PLAYER_ENTITY_TYPE = 155
_ITEM_ENTITY_TYPE = 71

def _build_entity_data(client: MCClient, jsondata: dict) -> tuple[int, int, str, Vector3f, Angle, Vector3] | None:
    """Parse common entity fields from the packet data.

    Returns (entityid, entitytype, uuid, pos3f, angle, pos) or None if the
    entity type should be ignored.
    """
    entityid = jsondata["entityId"]
    entitytype = jsondata["type"]
    if entitytype in _IGNORED_ENTITY_TYPES:
        return None

    uuid = jsondata["objectUUID"]
    pos3f = Vector3f(jsondata["x"], jsondata["y"], jsondata["z"])
    angle = Angle(jsondata["yaw"], jsondata["pitch"])
    client.entities[entityid] = MCEntity(pos3f, angle, entitytype)
    pos = pos3f.convert().to_vec3()
    return entityid, entitytype, uuid, pos3f, angle, pos


def _handle_player_spawn(
    client: MCClient, entityid: int, uuid: str, pos: Vector3, angle: Angle,
) -> None:
    """Send AOI enter packet for a player entity."""
    if uuid not in client.players:
        logger.warning(f"Cannot find player info: {uuid}")
        client.add_player_count += 1
        client.players[uuid] = {"name": "Unknown", "uin": client.add_player_count}

    client.entities[entityid].uin = client.players[uuid]["uin"]
    client.players[uuid]["entityid"] = entityid
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_ENTER_AOI_HC,
        PB_ActorEnterAOIHC(
            ObjID=client.players[uuid]["uin"],
            ActorType=1,
            ActorInfo=PB_ActorInfo(
                RoleInfo=PB_ActorRoleInfo(
                    Info=PB_RoleInfo(
                        Model=1,
                        NickName=client.players[uuid]["name"],
                        SkinID=skin.random_skin(),
                    ),
                    Player=PB_PlayerInfo(
                        RoleData=PB_RoleData(
                            Uin=client.players[uuid]["uin"],
                            HP=100,
                            Pos=PB_Pos(X=pos.x, Y=pos.y, Z=pos.z, Map=0),
                            Dir=PB_BodyDir(
                                RotationYaw=angle.to_mini_yaw_float(),
                                RotationPitch=angle.to_mini_pitch_float(),
                            ),
                        )
                    ),
                )
            ),
        ).SerializeToString(),
    )


def _handle_mob_spawn(
    client: MCClient, entityid: int, entitytype: int, pos: Vector3, angle: Angle,
) -> None:
    """Send AOI enter packet for a mob/non-player entity."""
    mini_obj_id = MINI_OBJ_ID_BASE + entityid
    if entityid in client.entities:
        client.miniplayer.send_packet(
            ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
            PB_ActorLeaveAOIHC(ObjID=mini_obj_id).SerializeToString(),
        )

    client.miniplayer.send_packet(
        ePBMsgCode.PB_GENERAL_ENTER_AOI_HC,
        PB_GeneralEnterAOIHC(
            ObjID=mini_obj_id,
            MapId=0,
            ActorMob=PB_ActorMob(
                defid=mob_mapping.mc_to_mini(entitytype),
                basedata=PB_ActorCommon(
                    wid=mini_obj_id,
                    pos=pos.to_mini(),
                    motion=Vector3().to_mini(),
                    yaw=angle.to_mini_yaw_int32(),
                    pitch=angle.to_mini_pitch_int32(),
                    flags=0,
                    falldist=0,
                    liveticks=0,
                    attinfo=PB_ActorAttInfo(),
                    masterobjid=0,
                    teamid=201,
                    cancollide=True,
                ),
                hp=100,
            ),
        ).SerializeToString(),
    )

def _handle_item_spawn(client: MCClient, entityid: int, pos: Vector3, angle: Angle):
    """Send AOI enter packet for a item entity."""
    mini_obj_id = MINI_OBJ_ID_BASE + entityid
    if entityid in client.entities:
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
                    pos=pos.to_mini(),
                    motion=Vector3().to_mini(),
                    yaw=angle.to_mini_yaw_int32(),
                    pitch=angle.to_mini_pitch_int32(),
                    flags=0,
                    falldist=0,
                    liveticks=0,
                    attinfo=PB_ActorAttInfo(),
                    masterobjid=0,
                    cancollide=True,
                ),
                itemid=100,
                num=1,
                durable=-1
            )
        ).SerializeToString(),
    )

def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Handle MC spawn_entity and create Mini World AOI entries.

    Parses common entity data, then dispatches to player or mob spawn
    handlers based on entity type.
    """
    entity_data = _build_entity_data(client, jsondata)
    if entity_data is None:
        return

    entityid, entitytype, uuid, _pos3f, angle, pos = entity_data
    if entitytype == _PLAYER_ENTITY_TYPE:
        _handle_player_spawn(client, entityid, uuid, pos, angle)
    elif entitytype == _ITEM_ENTITY_TYPE:
        _handle_item_spawn(client, entityid, pos, angle)
    else:
        _handle_mob_spawn(client, entityid, entitytype, pos, angle)


add_event("spawn_entity", on_recv)

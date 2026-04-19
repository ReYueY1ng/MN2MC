from loguru import logger

import mn2mc.mapping.mobs as mob_mapping
import mn2mc.mini.skin as skin
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
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
    PB_ActorAttInfo,
)
from mn2mc.mini.proto.hc import (
    PB_ActorEnterAOIHC,
    PB_GeneralEnterAOIHC,
    PB_ActorLeaveAOIHC,
)
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f, Vector3


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    entityid = jsondata["entityId"]
    entitytype = jsondata["type"]
    if entitytype in (5, 71):  # armor stand / item
        return
    uuid = jsondata["objectUUID"]
    pos3f = Vector3f(jsondata["x"], jsondata["y"], jsondata["z"])
    angle = Angle(jsondata["yaw"], jsondata["pitch"])
    client.entities[entityid] = {"pos": pos3f, "angle": angle}
    pos = pos3f.convert().to_vec3()
    if entitytype == 155:  # player
        if uuid not in client.players:
            logger.warning(f"Cannot find player info: {uuid}")
            client.add_player_count += 1
            client.players[uuid] = {"name": "Unknown", "uin": client.add_player_count}

        client.entities[entityid]['uin'] = client.players[uuid]['uin']
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
    else:
        if entityid in client.entities:
            client.miniplayer.send_packet(
                ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
                PB_ActorLeaveAOIHC(ObjID=4294967294 + entityid).SerializeToString(),
            )

        client.miniplayer.send_packet(
            ePBMsgCode.PB_GENERAL_ENTER_AOI_HC,
            PB_GeneralEnterAOIHC(
                ObjID=4294967294 + entityid,
                MapId=0,
                ActorMob=PB_ActorMob(
                    defid=mob_mapping.mc_to_mini(entitytype),
                    basedata=PB_ActorCommon(
                        wid=4294967294 + entityid,
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


add_event("spawn_entity", on_recv)

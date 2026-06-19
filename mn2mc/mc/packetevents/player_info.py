"""Handle MC player_info and synchronize player list with Mini World AOI."""

from __future__ import annotations

import mn2mc.mini.skin as skin
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.hc import PB_ActorLeaveAOIHC
from mn2mc.mini.proto.common import (
    PB_ActorInfo,
    PB_ActorRoleInfo,
    PB_BodyDir,
    PB_PlayerInfo,
    PB_Pos,
    PB_RoleData,
    PB_RoleInfo,
    ePBMsgCode,
)
from mn2mc.mini.proto.hc import PB_ActorEnterAOIHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Synchronize player additions/updates to Mini World.

    Sends leave+enter AOI packets for tracked players and registers
    unknown players for later entity mapping.
    """
    # print(jsondata)
    # client.add_player_count += 1
    if jsondata["action"]["add_player"]:
        for data in jsondata["data"]:
            uuid = data["uuid"]
            if uuid in client.players:
                if "entityid" not in client.players[uuid]:
                    continue
                objid = client.players[uuid]["uin"]
                entityid = client.players[uuid]["entityid"]
                pos = client.entities[entityid].pos.convert().to_vec3()
                client.players[uuid]["name"] = data["player"]["name"]
                client.miniplayer.send_packet(
                    ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
                    PB_ActorLeaveAOIHC(ObjID=objid).SerializeToString(),
                )
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
                                        Pos=PB_Pos(
                                            X=pos.x,
                                            Y=pos.y,
                                            Z=pos.z,
                                            Map=0,
                                        ),
                                        Dir=PB_BodyDir(
                                            RotationYaw=client.entities[entityid].angle.to_mini_yaw_float(),
                                            RotationPitch=client.entities[entityid].angle.to_mini_pitch_float(),
                                        ),
                                    )
                                ),
                            )
                        ),
                    ).SerializeToString(),
                )
            else:
                client.add_player_count += 1
                client.players[uuid] = {
                    "name": data["player"]["name"],
                    "uin": client.add_player_count,
                }


add_event("player_info", on_recv)

"""Handle MC entity look packets and forward as Mini World actor move."""

from __future__ import annotations

from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import (
    ePBMsgCode,
    PB_MoveMotion,
)
from mn2mc.mini.proto.hc import PB_ActorMoveHC
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Send an entity's new look angle to Mini World.

    Ignores entities not tracked by the proxy and converts MC yaw/pitch
    to Mini World format.
    """
    entityid = jsondata["entityId"]
    if entityid not in client.entities:
        return
    for _, player in client.players.items():
        if "entityid" in player and player["entityid"] == entityid:
            objid = player["uin"]
            break
    else:
        objid = MINI_OBJ_ID_BASE + entityid
    pos3f = client.entities[entityid]["pos"]
    pos = pos3f.convert().to_vec3().to_mini()
    angle = Angle.from_mc_int8(jsondata["yaw"], jsondata["pitch"])
    yaw, pitch = angle.to_mini_uint8()
    client.entities[entityid]["angle"] = angle
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_MOVE_HC,
        PB_ActorMoveHC(
            ObjID=objid,
            MoveMotion=PB_MoveMotion(
                Position=pos,
                Yaw=yaw,
                Pitch=pitch,
                ChangeFlags=0,
            ),
        ).SerializeToString(),
    )


add_event("entity_look", on_recv)

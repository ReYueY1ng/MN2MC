"""Handle MC entity move+look packets and forward as Mini World actor move."""

from __future__ import annotations

from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import (
    PB_MoveMotion,
    ePBMsgCode,
)
from mn2mc.mini.proto.hc import PB_ActorMoveHC
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Send an entity's new position and look to Mini World.

    Applies fixed-point delta movement, converts angles, and broadcasts
    PB_ACTOR_MOVE_HC.
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
    pos3f = client.entities[entityid].pos
    pos3f.x += jsondata["dX"] / (1 << 12)
    pos3f.y += jsondata["dY"] / (1 << 12)
    pos3f.z += jsondata["dZ"] / (1 << 12)
    pos = pos3f.convert().to_vec3().to_mini()
    angle = Angle.from_mc_int8(jsondata["yaw"], jsondata["pitch"])
    yaw, pitch = angle.to_mini_uint8()
    client.entities[entityid].angle = angle
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


add_event("entity_move_look", on_recv)

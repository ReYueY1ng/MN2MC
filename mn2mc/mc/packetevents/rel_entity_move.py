"""Handle MC relative entity movement and forward as Mini World actor move."""

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
    """Apply relative deltas to an entity and broadcast Mini World movement.

    Ignores missing or self entities and preserves stored yaw/pitch.
    """
    entityid = jsondata["entityId"]
    if entityid not in client.entities:
        return
    if entityid == -1:
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
    angle: Angle = client.entities[entityid].angle
    yaw, pitch = angle.to_mini_uint8()
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


add_event("rel_entity_move", on_recv)

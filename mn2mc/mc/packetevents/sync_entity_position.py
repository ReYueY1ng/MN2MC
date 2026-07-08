"""Handle MC sync_entity_position and broadcast Mini World actor movement."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import (
    PB_MoveMotion,
    ePBMsgCode,
)
from mn2mc.mini.proto.hc import PB_ActorMoveHC
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Update an entity's absolute position/angle and broadcast movement.

    Ignores entities not tracked by the proxy and maps IDs back to Mini
    World object IDs.
    """
    entityid = jsondata["entityId"]
    objid = client.resolve_objid(entityid)
    if objid is None:
        return
    pos3f = Vector3f(jsondata["x"], jsondata["y"], jsondata["z"])
    angle = Angle(jsondata["yaw"], jsondata["pitch"])
    client.entities[entityid].pos = pos3f
    client.entities[entityid].angle = angle
    if client.entities[entityid].type == 71:
        pos3f.y += 0.12 # 防止物品遁地
    pos = pos3f.convert().to_vec3().to_mini()
    yaw, pitch = angle.to_mini_uint8()
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_MOVE_HC,
        PB_ActorMoveHC(
            ObjID=objid,
            MoveMotion=PB_MoveMotion(
                Position=pos, Yaw=yaw, Pitch=pitch, MapID=0, ChangeFlags=0
            ),
        ).SerializeToString(),
    )


add_event("sync_entity_position", on_recv)

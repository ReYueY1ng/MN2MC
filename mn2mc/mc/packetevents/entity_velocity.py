"""Handle MC entity_velocity and forward as Mini World actor motion."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorMotionHC
from mn2mc.utils.vector import Vector3f


def on_recv(client: MCClient, jsondata: dict, _metadata: dict) -> None:
    """Apply velocity to an entity and forward to Mini World as motion.

    Input velocity is already in blocks/tick (node-minecraft-protocol
    applies the /8000 conversion internally).  PB_ActorMotionHC expects
    centi-blocks/tick, hence the /100 scaling.

    Ignores untracked entities.
    """
    # 注意：原版 node-minecraft-protocol 的 lpVec3 实现有问题（#1494），velocity 会变乱，需要手动 patch:
    # https://github.com/atiweb/node-minecraft-protocol/blob/64c8cee434a24a08a050ef73c471075b160a3f64/src/datatypes/lpVec3.js
    entityid = jsondata["entityId"]
    vel = Vector3f.from_dict(jsondata["velocity"])
    objid = client.resolve_objid(entityid)
    if objid is None:
        return
    if entityid in client.entities:
        client.entities[entityid].motion = vel

    vel = vel.convert()
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_MOTION_HC,
        PB_ActorMotionHC(
            ObjID=objid,
            x=vel.x / 100,
            y=vel.y / 100,
            z=vel.z / 100,
            isChangePos=False,
        ).SerializeToString(),
    )


add_event("entity_velocity", on_recv)

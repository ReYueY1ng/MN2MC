"""Handle MC entity_velocity and forward as Mini World actor motion."""

from __future__ import annotations

from mn2mc.constants import VELOCITY_SCALING
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorMotionHC
from mn2mc.utils.vector import Vector3f


def on_recv(client: MCClient, jsondata: dict, _metadata: dict) -> None:
    """Apply velocity to an entity and forward to Mini World as motion.

    Input velocity is in blocks/tick (native lpVec3 units since 1.21.9,
    vec3i16 units for older versions).

    Ignores untracked entities.
    """
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
            x=vel.x * VELOCITY_SCALING,
            y=vel.y * VELOCITY_SCALING,
            z=vel.z * VELOCITY_SCALING,
            isChangePos=False,
        ).SerializeToString(),
    )


add_event("entity_velocity", on_recv)

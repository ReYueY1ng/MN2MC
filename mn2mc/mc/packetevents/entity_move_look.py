"""Handle MC entity move+look packets and forward as Mini World actor move."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents._entity_move import broadcast_actor_move
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Send an entity's new position and look to Mini World.

    Applies fixed-point delta movement, converts angles, and broadcasts
    PB_ACTOR_MOVE_HC.
    """
    entityid = jsondata["entityId"]
    objid = client.resolve_objid(entityid)
    if objid is None:
        return
    pos3f = client.entities[entityid].pos
    pos3f.x += jsondata["dX"] / (1 << 12)
    pos3f.y += jsondata["dY"] / (1 << 12)
    pos3f.z += jsondata["dZ"] / (1 << 12)
    angle = Angle.from_mc_int8(jsondata["yaw"], jsondata["pitch"])
    client.entities[entityid].angle = angle
    broadcast_actor_move(client, objid, pos3f, angle)


add_event("entity_move_look", on_recv)

"""Handle MC entity look packets and forward as Mini World actor move."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents._entity_move import broadcast_actor_move
from mn2mc.utils.angle import Angle


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Send an entity's new look angle to Mini World.

    Ignores entities not tracked by the proxy and converts MC yaw/pitch
    to Mini World format.
    """
    entityid = jsondata["entityId"]
    objid = client.resolve_objid(entityid)
    if objid is None:
        return
    pos3f = client.entities[entityid].pos
    angle = Angle.from_mc_int8(jsondata["yaw"], jsondata["pitch"])
    client.entities[entityid].angle = angle
    broadcast_actor_move(client, objid, pos3f, angle)


add_event("entity_look", on_recv)

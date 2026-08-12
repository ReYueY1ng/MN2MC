"""Handle MC relative entity movement and forward as Mini World actor move."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents._entity_move import broadcast_actor_move


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Apply relative deltas to an entity and broadcast Mini World movement.

    Ignores missing or self entities and preserves stored yaw/pitch.
    """
    entityid = jsondata["entityId"]
    if entityid == -1:
        return
    objid = client.resolve_objid(entityid)
    if objid is None:
        return
    pos3f = client.entities[entityid].pos
    pos3f.x += jsondata["dX"] / (1 << 12)
    pos3f.y += jsondata["dY"] / (1 << 12)
    pos3f.z += jsondata["dZ"] / (1 << 12)
    angle = client.entities[entityid].angle
    broadcast_actor_move(client, objid, pos3f, angle)


add_event("rel_entity_move", on_recv)

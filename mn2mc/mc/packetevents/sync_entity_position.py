"""Handle MC sync_entity_position and broadcast Mini World actor movement."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents._entity_move import broadcast_actor_move
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
        pos3f.y += 0.12  # 防止物品遁地
    broadcast_actor_move(client, objid, pos3f, angle, map_id=0)


add_event("sync_entity_position", on_recv)

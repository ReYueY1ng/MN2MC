"""Shared helper for entity movement packet handlers."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mini.proto.common import PB_MoveMotion, ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorMoveHC
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f


def broadcast_actor_move(
    client: MCClient, objid: int, pos3f: Vector3f, angle: Angle, *, map_id: int | None = None
) -> None:
    """Build and send a PB_ACTOR_MOVE_HC packet to Mini World.

    Converts *pos3f* and *angle* to Mini World wire format and broadcasts
    via the player's RakNet connection.  When *map_id* is not ``None`` it
    is included in the ``PB_MoveMotion`` (protobuf wire fidelity).
    """
    pos = pos3f.convert().to_vec3().to_mini()
    yaw, pitch = angle.to_mini_uint8()
    move_kw: dict = {"Position": pos, "Yaw": yaw, "Pitch": pitch, "ChangeFlags": 0}
    if map_id is not None:
        move_kw["MapID"] = map_id
    client.miniplayer.send_packet(
        ePBMsgCode.PB_ACTOR_MOVE_HC,
        PB_ActorMoveHC(ObjID=objid, MoveMotion=PB_MoveMotion(**move_kw)).SerializeToString(),
    )

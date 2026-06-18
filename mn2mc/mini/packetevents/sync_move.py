"""Handle Mini World movement sync and translate to MC position/look packets."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.utils.vector import Vector3
from mn2mc.utils.angle import Angle


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Synchronize player position and view angles.

    Sends position_look, position, or look depending on which fields
    changed since the last packet.
    """
    move = proto.ch.PB_MoveSyncCH()
    move.ParseFromString(mcp.data)
    vec3f = Vector3.from_mini(move.pos).convert().to_vec3f()
    has_angle = move.HasField("move_opera")
    angle = Angle.from_mini_int32(move.move_opera.yaw, move.move_opera.pitch)
    if vec3f != player.mcclient.position and has_angle:
        player.mcclient.position = vec3f
        player.mcclient.angle = angle
        player.mcclient.send(
            "position_look",
            {
                "x": vec3f.x,
                "y": vec3f.y,
                "z": vec3f.z,
                "yaw": angle.yaw,
                "pitch": angle.pitch,
                "flags": 0x00,
            },
        )
    elif vec3f != player.mcclient.position:
        player.mcclient.position = vec3f
        player.mcclient.send(
            "position", {"x": vec3f.x, "y": vec3f.y, "z": vec3f.z, "flags": 0x00}
        )
    elif has_angle:
        player.mcclient.angle = angle
        player.mcclient.send(
            "look", {"yaw": angle.yaw, "pitch": angle.pitch, "flags": 0x00}
        )


add_event(proto.common.ePBMsgCode.PB_SYNC_MOVE_CH, on_recv)

"""Handle Mini World block punch packets and translate to MC block_dig."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.utils.vector import Vector3
import mn2mc.mapping.face as face_mapping


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Translate Mini World block punch to MC block_dig packet.

    Normalizes Mini World punch status and converts position/face to
    MC format.
    """
    punch = proto.ch.PB_BlockPunchCH()
    punch.ParseFromString(mcp.data)

    if punch.status == 2:
        punch.status = 1
    elif punch.status == 1:
        punch.status = 2

    pos = Vector3.from_mini(punch.blockpos).convert()
    pos.x -= 1

    player.mcclient.send(
        "block_dig",
        {
            "face": face_mapping.mini_to_mc(punch.face),
            "status": punch.status,
            "location": pos.to_dict(),
            "sequence": player.mcclient.block_sequence,
        },
    )


add_event(proto.common.ePBMsgCode.PB_BLOCK_PUNCH_CH, on_recv)

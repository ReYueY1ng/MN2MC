"""Handle Mini World block interact packets and translate to MC block_place."""

from __future__ import annotations

import mn2mc.mapping.face as face_mapping
import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer
from mn2mc.utils.vector import Vector3


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Translate Mini World block interact to MC block_place packet.

    Converts Mini World block position and face to MC format and sends
    block_place with default cursor values.
    """
    interact = proto.ch.PB_BlockInteractCH()
    interact.ParseFromString(mcp.data)
    pos = Vector3.from_mini(interact.blockpos).convert()
    pos.x -= 1
    player.mcclient.send(
        "block_place",
        {
            "hand": 0,
            "direction": face_mapping.mini_to_mc(interact.face),
            "cursorX": 0,
            "cursorY": 0,
            "cursorZ": 0,
            "location": pos.to_dict(),
            "sequence": player.mcclient.block_sequence,
            "insideBlock": False,
            "worldBorderHit": False,
        },
    )


add_event(proto.common.ePBMsgCode.PB_BLOCK_INTERACT_CH, on_recv)

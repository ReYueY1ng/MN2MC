"""Handle Mini World actor interact packets and translate to MC use_entity."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.constants import MINI_OBJ_ID_BASE


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Translate Mini World actor interact to MC use_entity packet.

    Maps Mini World target IDs to MC entity IDs and sends use_entity
    with mouse=0 (interact).
    """
    interact = proto.ch.PB_ActorInteractCH()
    interact.ParseFromString(mcp.data)
    for _, mcplayer in player.mcclient.players.items():
        if mcplayer["uin"] == interact.target:
            entityid = mcplayer["entityid"]
            break
    else:
        if interact.target > MINI_OBJ_ID_BASE - 1:
            entityid = interact.target - MINI_OBJ_ID_BASE
        else:
            for eid, entity in player.mcclient.entities.items():
                if entity.uin == interact.target:
                    entityid = eid
            else:
                entityid = interact.target
    player.mcclient.send(
        "use_entity", {"target": entityid, "mouse": 0, "hand": 0, "sneaking": False}
    )


add_event(proto.common.ePBMsgCode.PB_ACTOR_INTERACT_CH, on_recv)

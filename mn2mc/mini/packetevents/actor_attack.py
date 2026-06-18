"""Handle Mini World actor attack packets and translate to MC use_entity."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.constants import MINI_OBJ_ID_BASE
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Translate Mini World actor attack to MC use_entity packet.

    Maps Mini World target IDs to MC entity IDs and sends use_entity
    with mouse=1 (attack).
    """
    attack = proto.ch.PB_ActorAttackCH()
    attack.ParseFromString(mcp.data)
    for objid in attack.targetIds:
        for _, mcplayer in player.mcclient.players.items():
            if mcplayer["uin"] == objid:
                entityid = mcplayer["entityid"]
                break
        else:
            if objid > MINI_OBJ_ID_BASE - 1:
                entityid = objid - MINI_OBJ_ID_BASE
            else:
                for eid, entity in player.mcclient.entities.items():
                    if 'uin' in entity and entity['uin'] == objid:
                        entityid = eid
                else:
                    entityid = objid
        player.mcclient.send(
            "use_entity", {"target": entityid, "mouse": 1, "sneaking": False}
        )


add_event(proto.common.ePBMsgCode.PB_ACTOR_ATTACK_CH, on_recv)

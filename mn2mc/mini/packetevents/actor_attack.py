import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket):
    attack = proto.ch.PB_ActorAttackCH()
    attack.ParseFromString(mcp.data)
    for objid in attack.targetIds:
        for _, mcplayer in player.mcclient.players.items():
            if mcplayer["uin"] == objid:
                entityid = mcplayer["entityid"]
                break
        else:
            if objid > 4294967293:
                entityid = objid - 4294967294
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

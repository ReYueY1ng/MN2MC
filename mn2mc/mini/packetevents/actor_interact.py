import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket):
    interact = proto.ch.PB_ActorInteractCH()
    interact.ParseFromString(mcp.data)
    for _, mcplayer in player.mcclient.players.items():
        if mcplayer["uin"] == interact.target:
            entityid = mcplayer["entityid"]
            break
    else:
        if interact.target > 4294967293:
            entityid = interact.target - 4294967294
        else:
            for eid, entity in player.mcclient.entities.items():
                if 'uin' in entity and entity['uin'] == interact.target:
                    entityid = eid
            else:
                entityid = interact.target
    player.mcclient.send(
        "use_entity", {"target": entityid, "mouse": 0, "hand": 0, "sneaking": False}
    )


add_event(proto.common.ePBMsgCode.PB_ACTOR_INTERACT_CH, on_recv)

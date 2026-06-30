import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    player.mcclient.send("client_command", {"actionId": 0})


add_event(proto.common.ePBMsgCode.PB_ACTOR_REVIVE_CH, on_recv)

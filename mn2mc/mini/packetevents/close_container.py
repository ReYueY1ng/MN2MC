import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket):
    player.mcclient.window_id = 0
    #player.mcclient.inventory_type = "inventory"
    player.mcclient.send("close_window", {"windowId": player.mcclient.window_id})


add_event(proto.common.ePBMsgCode.PB_CLOSE_CONTAINER_CH, on_recv)

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket):
    select = proto.ch.PB_PlayerSelectShortcutCH()
    select.ParseFromString(mcp.data)
    player.mcclient.send("held_item_slot", {"slotId": select.index})


add_event(proto.common.ePBMsgCode.PB_PLAYER_SELECTSHORTCUT_CH, on_recv)

"""Handle Mini World shortcut selection and translate to MC held_item_slot."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Select a hotbar slot on the MC client.

    Forwards the Mini World shortcut index as a held_item_slot packet.
    """
    select = proto.ch.PB_PlayerSelectShortcutCH()
    select.ParseFromString(mcp.data)
    player.mcclient.send("held_item_slot", {"slotId": select.index})


add_event(proto.common.ePBMsgCode.PB_PLAYER_SELECTSHORTCUT_CH, on_recv)

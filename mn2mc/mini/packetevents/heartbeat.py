"""Handle Mini World heartbeat packets and echo them back."""

from __future__ import annotations

import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Echo the heartbeat beat code back to the Mini World client.

    Keeps the connection alive by responding with the same beat code.
    """
    heartbeat_ch = proto.ch.PB_HeartBeatCH()
    heartbeat_ch.ParseFromString(mcp.data)
    heartbeat_hc = proto.hc.PB_HeartBeatHC(BeatCode=heartbeat_ch.BeatCode)
    player.send_packet(
        proto.common.ePBMsgCode.PB_HEARTBEAT_HC,
        heartbeat_hc.SerializeToString(),
    )


add_event(proto.common.ePBMsgCode.PB_HEARTBEAT_CH, on_recv)

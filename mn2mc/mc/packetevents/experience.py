"""Handle MC experience update and synchronize to Mini World."""

from __future__ import annotations

import math

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_PlayerAttrChangeHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Synchronize MC experience bar/level to Mini World player level UI."""
    bar = jsondata.get("experienceBar", 0.0)  # 0..1
    level = jsondata.get("level", 0)  # varint

    client.miniplayer.send_packet(
        ePBMsgCode.PB_PLAYER_ATTR_CHANGE_HC,
        PB_PlayerAttrChangeHC(
            Exp=math.floor(level * 100 + bar * 100)
        ).SerializeToString(),
    )


add_event("experience", on_recv)

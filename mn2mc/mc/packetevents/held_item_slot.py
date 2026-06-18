"""Handle MC held_item_slot changes."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
# from mn2mc.mini.proto.hc import PB_


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Process held hotbar slot changes from the MC client.

    Slot value is currently received but not forwarded to Mini World.
    """
    slot = jsondata["slot"]
    # maybe custom msg?


add_event("held_item_slot", on_recv)

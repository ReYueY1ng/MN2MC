"""Handle MC acknowledge_player_digging and track block sequence."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Update the client block action sequence after a dig acknowledgement.

    Stores the server-provided sequence ID for subsequent block packets.
    """
    client.block_sequence = jsondata["sequenceId"]


add_event("acknowledge_player_digging", on_recv)

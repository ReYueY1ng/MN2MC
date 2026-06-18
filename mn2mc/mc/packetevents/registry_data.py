"""Handle MC registry_data and cache dimension codec information."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
# from mn2mc.mini.proto.hc import PB_


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Cache dimension codec data from registry_data packets.

    Currently only stores the 'minecraft:dimension_type' registry entry.
    """
    if jsondata['id'] == "minecraft:dimension_type":
        client.registry.loadDimensionCodec(jsondata)


add_event("registry_data", on_recv)

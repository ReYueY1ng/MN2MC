"""Handle MC close_window and notify Mini World to close the container."""

from __future__ import annotations

import time

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_CloseContainerHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Close the current container on the Mini World client.

    Resets tracked window state, clears any pending items,
    and sends PB_CLOSE_CONTAINER_HC.
    """
    client.window_id = 0
    client.inventory_type = "inventory"
    client.container_ts = time.time()
    with client._lock:
        client._pending_item_packets.clear()
    client.miniplayer.send_packet(
        ePBMsgCode.PB_CLOSE_CONTAINER_HC,
        PB_CloseContainerHC(
            BaseIndex=3000,
        ).SerializeToString(),
    )


add_event("close_window", on_recv)

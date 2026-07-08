"""Handle MC open_window and notify Mini World of container properties."""

from __future__ import annotations

import threading
import time

from loguru import logger

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_CloseContainerHC, PB_OpenContainerHC


def _flush_pending_items(client: MCClient) -> None:
    with client._lock:
        items = list(client._pending_item_packets)
        client._pending_item_packets.clear()
    for msgcode, data in items:
        client.miniplayer.send_packet(msgcode, data)


def _do_open_container(client: MCClient) -> None:
    client._open_timer = None
    client._open_pending = False
    client.miniplayer.send_packet(
        ePBMsgCode.PB_OPEN_CONTAINER_HC,
        PB_OpenContainerHC(
            BaseIndex=3000, TotalItemGrids=client._pending_grids
        ).SerializeToString(),
    )
    _flush_pending_items(client)


def _schedule_open(client: MCClient, grids: int) -> None:
    if getattr(client, "_open_pending", False):
        client._pending_grids = grids
        return
    client._open_pending = True
    client._pending_grids = grids
    client._open_timer = threading.Timer(0.1, _do_open_container, args=[client])
    client._open_timer.start()  # ty:ignore[unresolved-attribute]


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    window_id = jsondata["windowId"]
    inventory_type = jsondata["inventoryType"]
    origin_type = client.inventory_type

    match inventory_type:
        case 0:
            grids = 9
        case 1:
            grids = 18
        case 2:
            grids = 27
        case 3:
            grids = 36
        case 4:
            grids = 45
        case 5:
            grids = 54
        case 6:
            grids = 9
        case 7:
            grids = 9
        case _:
            grids = 27
            logger.warning(f"Inventory type {inventory_type} was not supported")

    client.window_id = window_id
    client.inventory_type = inventory_type
    curtime = time.time()

    if getattr(client, "_open_pending", False):
        client._pending_grids = grids
        return

    if origin_type != "inventory":
        client.miniplayer.send_packet(
            ePBMsgCode.PB_CLOSE_CONTAINER_HC,
            PB_CloseContainerHC(BaseIndex=3000).SerializeToString(),
        )
        client.container_ts = time.time()
        _schedule_open(client, grids)
        return

    if client.container_ts + 0.5 > curtime:
        logger.info("Open container too quick! Delaying...")
        client.container_ts = time.time()
        _schedule_open(client, grids)
        return

    client.container_ts = time.time()
    client.miniplayer.send_packet(
        ePBMsgCode.PB_OPEN_CONTAINER_HC,
        PB_OpenContainerHC(
            BaseIndex=3000, TotalItemGrids=grids
        ).SerializeToString(),
    )


add_event("open_window", on_recv)

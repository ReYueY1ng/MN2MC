"""Handle MC open_window and notify Mini World of container properties."""

from __future__ import annotations
import threading
import time

from loguru import logger
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_OpenContainerHC, PB_CloseContainerHC


def _send_open_container(client: MCClient, grids: int) -> None:
    """Send open container packet (separated for Timer usage)."""
    client.miniplayer.send_packet(
        ePBMsgCode.PB_OPEN_CONTAINER_HC,
        PB_OpenContainerHC(BaseIndex=3000, TotalItemGrids=grids).SerializeToString(),
    )


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Translate MC open_window into Mini World container open.

    Maps MC inventory types to grid counts and sends PB_OPEN_CONTAINER_HC.
    """
    window_id = jsondata["windowId"]
    inventory_type = jsondata["inventoryType"]
    client.window_id = window_id
    client.inventory_type = inventory_type

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

    curtime = time.time()
    
    if client.inventory_type != 'inventory':
        client.miniplayer.send_packet(
            ePBMsgCode.PB_CLOSE_CONTAINER_HC,
            PB_CloseContainerHC(
                BaseIndex=3000,
            ).SerializeToString(),
        )
        client.container_ts = time.time()
        threading.Timer(0.1, _send_open_container, args=[client, grids]).start()
        return
    elif client.container_ts + 0.5 > curtime:
        logger.info('Open container too quick! Delaying...')
        client.container_ts = time.time()
        threading.Timer(0.1, _send_open_container, args=[client, grids]).start()
        return
    
    client.container_ts = time.time()
    _send_open_container(client, grids)


add_event("open_window", on_recv)

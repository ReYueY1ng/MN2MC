"""Handle MC open_window and notify Mini World of container properties."""

from __future__ import annotations

from loguru import logger
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_OpenContainerHC


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

    client.miniplayer.send_packet(
        ePBMsgCode.PB_OPEN_CONTAINER_HC,
        PB_OpenContainerHC(BaseIndex=3000, TotalItemGrids=grids).SerializeToString(),
    )


add_event("open_window", on_recv)

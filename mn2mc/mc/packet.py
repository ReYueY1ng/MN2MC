import importlib

from loguru import logger

import mn2mc.config as config
from mn2mc.events import add_event, del_event, events, reset_events  # noqa: F401

# NOTE: on_event is kept as a sync wrapper here because mc/client.py calls it
# synchronously from on_packet (JS bridge callback). The shared events.on_event
# is async (for mini side), but mc packet handlers are all sync functions.


def on_event(event: str, client: object, jsondata: dict, metadata: dict):
    """Sync dispatcher for mc packet events.

    Iterates handlers from the shared events registry. All mc packet handlers
    are sync functions, so no async bridging is needed.
    """
    if event not in events:
        events[event] = []
    for func in events[event]:
        if func is None:
            continue
        try:
            func(client, jsondata, metadata)
        except Exception as e:
            logger.exception(f"Exception occurred: {str(e)}")


def load_all_event():
    importlib.import_module("mn2mc.mc.packetevents")
    if config.mc["use_new_chunk_parser"]:
        importlib.import_module("mn2mc.mc.packetevents.chunk.parsed_chunk", __package__)
    else:
        importlib.import_module("mn2mc.mc.packetevents.chunk.map_chunk", __package__)

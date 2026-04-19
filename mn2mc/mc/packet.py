from loguru import logger
import importlib
import types
import mn2mc.config as config


events = {}


def add_event(event: str, func: types.FunctionType):
    __check_event(event)
    events[event].append(func)
    return len(events[event])


def del_event(event: str, id: int):
    __check_event(event)
    events[event][id] = None


def reset_events():
    global events
    events = {}


def __check_event(event: str):
    if event not in events:
        events[event] = []


def on_event(event: str, client: object, jsondata: dict, metadata: dict):
    __check_event(event)
    for func in events[event]:
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

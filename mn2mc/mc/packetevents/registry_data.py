from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
# from mn2mc.mini.proto.hc import PB_


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    if jsondata['id'] == "minecraft:dimension_type":
        client.registry.loadDimensionCodec(jsondata)


add_event("registry_data", on_recv)

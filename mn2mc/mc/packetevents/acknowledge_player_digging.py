from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    client.block_sequence = jsondata["sequenceId"]


add_event("acknowledge_player_digging", on_recv)

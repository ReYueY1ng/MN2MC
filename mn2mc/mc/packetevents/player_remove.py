from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    for uuid in jsondata["players"]:
        if uuid in client.players:
            del client.players[uuid]


add_event("player_remove", on_recv)

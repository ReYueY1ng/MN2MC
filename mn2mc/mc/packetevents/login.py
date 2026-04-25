import mn2mc
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_GameModeChangeHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    client.client.registerChannel("minecraft:brand", ["string", []])
    client.client.writeChannel(
        "minecraft:brand",
        f"Mini World {client.miniplayer.cltversion} | MN2MC {mn2mc.version}",
    )

    worldstate = jsondata["worldState"]
    client.dimension = worldstate['dimension']

    gm = 1
    oldgm = 3
    match worldstate["gamemode"]:
        case "survival":  # Survival
            gm = 1
            oldgm = 3
        case "creative":  # Creative
            gm = 3
            oldgm = 1
        case "adventure":  # Adventure
            gm = 1
            oldgm = 3
        case "spectator":  # Spectator
            gm = 3
            oldgm = 1

    gmc = PB_GameModeChangeHC(oldGameMode=gm, newGameMode=oldgm).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_GAME_MODE_CHANGE, gmc)


add_event("login", on_recv)

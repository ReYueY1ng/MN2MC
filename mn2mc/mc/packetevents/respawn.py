from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_GameModeChangeHC
import mn2mc.config as config
from javascript import require

registry = require("prismarine-registry")(config.mc["version"])


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    spawn_info = jsondata["worldState"]
    client.dimension = spawn_info['dimension']

    gm = 1
    oldgm = 3
    match spawn_info["gamemode"]:
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


add_event("respawn", on_recv)

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_GameModeChangeHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    if jsondata["reason"] == "change_game_mode":
        gm = 1
        oldgm = 3
        match jsondata["gameMode"]:
            case 0:  # Survival
                gm = 1
                oldgm = 3
            case 1:  # Creative
                gm = 3
                oldgm = 1
            case 2:  # Adventure
                gm = 1
                oldgm = 3
            case 3:  # Spectator
                gm = 3
                oldgm = 1

        gmc = PB_GameModeChangeHC(oldGameMode=gm, newGameMode=oldgm).SerializeToString()
        client.miniplayer.send_packet(ePBMsgCode.PB_GAME_MODE_CHANGE, gmc)


add_event("game_state_change", on_recv)

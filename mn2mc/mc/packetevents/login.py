"""Handle MC login and synchronize initial state to Mini World."""

from __future__ import annotations

import mn2mc
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.entity import MCEntity, entitytypes
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_GameModeChangeHC
from mn2mc.utils.vector import Vector3f
from mn2mc.utils.angle import Angle

def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Complete MC login handshake and send game mode to Mini World.

    Sends a brand channel message and broadcasts the initial game mode.
    """
    client.client.registerChannel("minecraft:brand", ["string", []])
    client.client.writeChannel(
        "minecraft:brand",
        f"Mini World {client.miniplayer.cltversion} | MN2MC {mn2mc.version}",
    )
    client.entityid = jsondata['entityId']
    client.entities[client.entityid] = MCEntity(Vector3f(), Angle(0,0), entitytypes.get('player', 0), uin=client.miniplayer.uin)

    worldstate = jsondata["worldState"]
    client.dimension = worldstate['dimension']

    gm = 1
    oldgm = 3
    # 注意：Mini World 的 gm/oldgm 与 MC 的 gamemode 是反向映射
    # MC survival → Mini gm=1(oldgm=3), MC creative → Mini gm=3(oldgm=1)
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

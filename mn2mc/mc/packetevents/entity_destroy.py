"""Handle MC entity_destroy and remove entities from Mini World AOI."""

from __future__ import annotations

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorLeaveAOIHC
from mn2mc.constants import MINI_OBJ_ID_BASE


def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Remove destroyed MC entities from Mini World.

    Maps entity IDs back to Mini World object IDs and broadcasts
    PB_ACTOR_LEAVE_AOI_HC to the Mini World client.
    """
    for entityid in jsondata["entityIds"]:
        for _, player in client.players.items():
            if "entityid" in player and player["entityid"] == entityid:
                objid = player["uin"]
                del player["entityid"]
                break
        else:
            objid = MINI_OBJ_ID_BASE + entityid
            if entityid in client.entities:
                if client.entities[entityid].uin is not None:
                    objid = client.entities[entityid].uin
                del client.entities[entityid]

        client.miniplayer.send_packet(
            ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
            PB_ActorLeaveAOIHC(ObjID=objid).SerializeToString(),
        )


add_event("entity_destroy", on_recv)

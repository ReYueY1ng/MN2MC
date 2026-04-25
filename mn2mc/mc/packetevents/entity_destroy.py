from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_ActorLeaveAOIHC


def on_recv(client: MCClient, jsondata: dict, metadata: dict):
    for entityid in jsondata["entityIds"]:
        for _, player in client.players.items():
            if "entityid" in player and player["entityid"] == entityid:
                objid = player["uin"]
                del player["entityid"]
                break
        else:
            objid = 4294967294 + entityid
            if entityid in client.entities:
                if 'uin' in client.entities[entityid]:
                    objid = client.entities[entityid]['uin']
                del client.entities[entityid]

        client.miniplayer.send_packet(
            ePBMsgCode.PB_ACTOR_LEAVE_AOI_HC,
            PB_ActorLeaveAOIHC(ObjID=objid).SerializeToString(),
        )


add_event("entity_destroy", on_recv)

"""Handle MC update_time — sync world time to Mini World."""

from __future__ import annotations

import javascript

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mini.proto.common import ePBMsgCode
from mn2mc.mini.proto.hc import PB_WGlobalUpdateHC

javascript.eval_js("BigInt.prototype.toJSON = function() { return Number(this); };")

def on_recv(client: MCClient, jsondata: dict, metadata: dict) -> None:
    """Forward MC world time to Mini World time display.

    MC sends worldAge and timeOfDay as longs (ticks).
    """
    time_of_day = int(jsondata['time'].valueOf())
    world_age = int(jsondata['age'].valueOf())

    msg = PB_WGlobalUpdateHC(
        WorldTime=world_age,
        DayNightTime=time_of_day,
        CurWeather=0
    ).SerializeToString()
    client.miniplayer.send_packet(ePBMsgCode.PB_WGLOBAL_UPDATE_HC, msg)


add_event("update_time", on_recv)

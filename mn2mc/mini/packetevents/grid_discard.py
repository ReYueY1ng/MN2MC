import mn2mc.mini.proto as proto
import mn2mc.mapping.slotid as slotid_mapping
from mn2mc.mini.player import MiniPlayer
from mn2mc.mini.packet import MiniClientPacket, add_event


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket):
    discard = proto.ch.PB_BackPackGridDiscardCH()
    discard.ParseFromString(mcp.data)

    if discard.GridId == 7000:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": -999,
                "mode": 0,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )
    else:
        player.mcclient.send(
            "window_click",
            {
                "windowId": player.mcclient.window_id,
                "stateId": player.mcclient.container_sequence,
                "slot": slotid_mapping.mini_to_mc(
                    player.mcclient.inventory_type, discard.GridId
                ),
                "mode": 4,
                "mouseButton": 0,
                "changedSlots": [],
            },
        )


add_event(proto.common.ePBMsgCode.PB_BACKPACK_GRID_DISCARD_CH, on_recv)

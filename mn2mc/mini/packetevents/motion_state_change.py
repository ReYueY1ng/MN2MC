import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    motion_state = proto.ch.PB_PlayerMotionStateChangeCH()
    motion_state.ParseFromString(mcp.data)

    if motion_state.StateType == 6: # sneak
        player.mcclient.send('player_input', {
            "inputs": {
                "shift": motion_state.StateSwitch
            }
        })


add_event(proto.common.ePBMsgCode.PB_PLAYER_MOTIONSTATECHANGE_CH, on_recv)

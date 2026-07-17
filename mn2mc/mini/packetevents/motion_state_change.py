import mn2mc.mini.proto as proto
from mn2mc.mini.enums import MotionStateType
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    motion_state = proto.ch.PB_PlayerMotionStateChangeCH()
    motion_state.ParseFromString(mcp.data)
    match motion_state.StateType:
        case MotionStateType.RUN:
            player.mcclient.send(
                "entity_action",
                {
                    "entityId": player.mcclient.entityid,
                    "actionId": "start_sprinting" if motion_state.StateSwitch else "stop_sprinting",
                },
            )
        case MotionStateType.JUMP:  # Mini World 似乎不会发 FallGround 类型，先用这个凑合一下
            player.mcclient.on_ground = not motion_state.StateSwitch
        case MotionStateType.SNEAK:
            player.mcclient.send("player_input", {"inputs": {"shift": motion_state.StateSwitch}})


add_event(proto.common.ePBMsgCode.PB_PLAYER_MOTIONSTATECHANGE_CH, on_recv)

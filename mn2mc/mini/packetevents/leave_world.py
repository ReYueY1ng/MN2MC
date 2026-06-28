from loguru import logger

import mn2mc.mini.proto as proto
from mn2mc.mini.packet import MiniClientPacket, add_event
from mn2mc.mini.player import MiniPlayer


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    logger.info(f"{player.name} left")
    player.kick()


add_event(proto.common.ePBMsgCode.PB_ROLE_LEAVE_WORLD_CH, on_recv)

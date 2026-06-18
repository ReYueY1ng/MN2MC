"""Handle Mini World chat packets, commands, and relay to MC chat."""

from __future__ import annotations

from loguru import logger
import mn2mc
import mn2mc.mini.proto as proto
from mn2mc.mini.player import MiniPlayer, players
from mn2mc.mini.packet import (
    MiniClientPacket,
    add_event,
    reset_events as mini_reset_events,
)
from mn2mc.mc.packet import reset_events as mc_reset_events
import mn2mc.utils.protobuf_parser as protobuf_parser
from importlib import reload
import mn2mc.config as config


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Process Mini World chat messages and /mn2mc commands.

    Handles /mn2mc version, reload, and respawn commands; relays all
    other messages to the MC server via client.chat().
    """
    chat_ch = proto.ch.PB_ChatCH()
    chat_ch.ParseFromString(mcp.data)
    # chat_hc = proto.hc.PB_ChatHC(ChatType=0, Uin=player.uin, Speaker=player.name, Content=chat_ch.Content, Language=1, Extend='{"buddle":1}')
    # broadcast_packet(proto.common.ePBMsgCode.PB_CHAT_HC, chat_hc.SerializeToString())
    if chat_ch.Content.startswith("/mn2mc"):
        args = chat_ch.Content.split(" ")[1:]
        if len(args) == 0:
            player.send_msg(f"[color=#aaeeee]MN2MC {mn2mc.version}", False)
            player.send_msg("[color=#aaeeee]github.com/ReYueY1ng/MN2MC")
            return

        match args[0]:
            case "version":
                player.send_msg(
                    f"[color=#aaeeee]MN2MC {mn2mc.version}\nPowered by YueY1ng", False
                )
            case "reload":
                logger.info("Reloading...")
                from mn2mc.mini.packetevents import reloadevents as mini_reloadevents
                from mn2mc.mc.packetevents import reloadevents as mc_reloadevents
                from mn2mc.mapping import reload_mapping

                mini_reset_events()
                mc_reset_events()
                mini_reloadevents()
                mc_reloadevents()
                reload_mapping()

                for player in players.copy():
                    player.mcclient.load_events()

                use_new_chunk_parser = config.mc['use_new_chunk_parser']
                config.load()
                config.mc['use_new_chunk_parser'] = use_new_chunk_parser
                if config.debug:
                    reload(protobuf_parser)
                    protobuf_parser.init()
                logger.info("Reloaded!")
            case "respawn":
                player.mcclient.send("client_command", {"actionId": 0})
    else:
        player.mcclient.chat(chat_ch.Content)


add_event(proto.common.ePBMsgCode.PB_CHAT_CH, on_recv)

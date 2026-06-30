"""Handle Mini World chat packets, commands, and relay to MC chat."""

from __future__ import annotations

import time
from importlib import reload

from loguru import logger

import mn2mc
import mn2mc.config as config
import mn2mc.mini.auth
import mn2mc.mini.proto as proto
import mn2mc.utils.protobuf_parser as protobuf_parser
from mn2mc.mc.packet import reset_events as mc_reset_events
from mn2mc.mini.packet import (
    MiniClientPacket,
    add_event,
)
from mn2mc.mini.packet import (
    reset_events as mini_reset_events,
)
from mn2mc.mini.player import MiniPlayer, players

# Per-player cooldown for /mn2mc commands (seconds)
_command_cooldowns: dict[int, float] = {}
_COMMAND_COOLDOWN_SECS = 5


async def on_recv(player: MiniPlayer, mcp: MiniClientPacket) -> None:
    """Process Mini World chat messages and /mn2mc commands.

    Handles /mn2mc version, reload, and respawn commands; relays all
    other messages to the MC server via client.chat().
    """
    chat_ch = proto.ch.PB_ChatCH()
    chat_ch.ParseFromString(mcp.data)
    if chat_ch.Content.startswith("/mn2mc"):
        args = chat_ch.Content.split(" ")[1:]
        if len(args) == 0:
            player.send_msg(f"[color=#aaeeee]MN2MC {mn2mc.version}", False)
            player.send_msg("[color=#aaeeee]github.com/ReYueY1ng/MN2MC")
            return

        # Check admin permission: whitelist
        is_admin = player.uin in config.mini["admin_uins"] if config.mini["admin_uins"] else False

        match args[0]:
            case "version":
                player.send_msg(
                    f"[color=#aaeeee]MN2MC {mn2mc.version}\nPowered by YueY1ng", False
                )
            case "reload" | "respawn":
                if not is_admin:
                    player.send_msg("#RPermission denied", False)
                    return
                # Cooldown check
                now = time.time()
                last = _command_cooldowns.get(player.uin, 0.0)
                if now - last < _COMMAND_COOLDOWN_SECS:
                    remaining = int(_COMMAND_COOLDOWN_SECS - (now - last))
                    player.send_msg(
                        f"#RCooldown: {remaining}s", False
                    )
                    return
                _command_cooldowns[player.uin] = now

                if args[0] == "reload":
                    logger.info("Reloading...")
                    from mn2mc.mapping import reload_mapping
                    from mn2mc.mc.packetevents import reloadevents as mc_reloadevents
                    from mn2mc.mini.packetevents import reloadevents as mini_reloadevents

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
                elif args[0] == "respawn":
                    player.mcclient.send("client_command", {"actionId": 0})
    else:
        player.mcclient.chat(chat_ch.Content)


add_event(proto.common.ePBMsgCode.PB_CHAT_CH, on_recv)

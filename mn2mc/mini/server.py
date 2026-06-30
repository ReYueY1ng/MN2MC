import json

import aiorak
from loguru import logger

import mn2mc
import mn2mc.config as config
import mn2mc.mini.auth
import mn2mc.mini.proto as proto
import mn2mc.mini.room
import mn2mc.mini.wsconn
from mn2mc.mc.packet import load_all_event as mc_load_all_event
from mn2mc.mini.packet import MiniServerPacket
from mn2mc.mini.packet import load_all_event as mini_load_all_event
from mn2mc.mini.player import MiniPlayer, _players_lock, players

default_extra_info = {
    "room_extra": {
        "audioconfigurl": '{"editorSceneSwitch":1,"worldtype":4 } ',
        "autoTag": "综合",
        "editorSceneSwitch": 0,
        "modUuids": [],
        "modurl": "",
        "translate": "",
        "translate_sourcelang": 0,
        "uilibsurl": "",
        "version": mn2mc.mini.version,
        "vipExp": 0,
        "vipLevel": 0,
        "vipType": 0,
    }
}


room_extra_info = proto.hc.PB_RoomExtraInfoHC()
room_extra_info.room_extra = json.dumps(default_extra_info["room_extra"]).encode()
# room_extra_info.CMURL = default_extra_info["CMURL"]
# room_extra_info.MapMD5 = default_extra_info["MapMD5"]
# room_extra_info.MapID = default_extra_info["MapID"]
room_extra_info_bytes = room_extra_info.SerializeToString()

miniserver: aiorak.Server


def broadcast_packet(msgcode: proto.common.ePBMsgCode, data: bytes):
    if config.mini["server"]["host_to_room_server"]:
        with _players_lock:
            for player in players:
                player.send_packet(msgcode, data)
    else:
        miniserver.broadcast(MiniServerPacket(msgcode, data).encode())


def send_log(msg: str):
    if config.mini["send_log_to_chat"]:
        broadcast_packet(
            proto.common.ePBMsgCode.PB_CHAT_HC,
            proto.hc.PB_ChatHC(ChatType=1, Uin=0, Content=msg[:-1]).SerializeToString(),
        )


async def handler(conn: aiorak.Connection):
    uin = conn.remote_guid
    logger.info(f"{uin} {conn.remote_address} connected")
    player = MiniPlayer(conn, uin)

    player.send_packet(
        proto.common.ePBMsgCode.PB_SYNC_ROOM_EXTRA_HC, room_extra_info_bytes
    )

    if config.mini["server"]["host_to_room_server"]:
        with _players_lock:
            player_count = len(players)
        await mn2mc.mini.room.room_update(player_count)

    await player.handler()
    player.kick()
    logger.info(f"{uin} {conn.remote_address} disconnected")

    if config.mini["server"]["host_to_room_server"]:
        with _players_lock:
            player_count = len(players) - 1
        await mn2mc.mini.room.room_update(player_count)


async def start(host: str = "0.0.0.0", port: int = 19132):
    global miniserver
    if config.mini["server"]["host_to_room_server"]:
        await mn2mc.mini.wsconn.fetch_s2()
        await mn2mc.mini.room.create_room()
    logger.info("Loading events...")
    mini_load_all_event()
    mc_load_all_event()
    miniserver = await aiorak.create_server(
        (host, port),
        handler,
        guid=mn2mc.mini.auth.uin
        if config.mini["server"]["host_to_room_server"]
        else 666,
        max_connections=mn2mc.config.mini['server']['max_players']
    )
    logger.info(f"Server started at {host}:{port}")
    logger.add(send_log, level="INFO", format="#W[{level}] {message}")

    await miniserver.serve_forever()


async def stop():
    with _players_lock:
        for player in players.copy():
            player.kick()
    if miniserver:
        await miniserver.close()
    if config.mini["server"]["host_to_room_server"] and mn2mc.mini.room.room_token:
        await mn2mc.mini.room.close_room()
    mn2mc.running = False

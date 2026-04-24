import json

import aiorak
from loguru import logger

import mn2mc
import mn2mc.mini.proto as proto
import mn2mc.config as config
from mn2mc.mini.packet import MiniServerPacket, load_all_event as mini_load_all_event
from mn2mc.mc.packet import load_all_event as mc_load_all_event
from mn2mc.mini.player import MiniPlayer, players

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
        "version": "1.54.1",
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

    await player.handler()
    player.kick()
    logger.info(f"{uin} {conn.remote_address} disconnected")


async def start(host: str = "0.0.0.0", port: int = 19132):
    global miniserver
    logger.info("Loading events...")
    mini_load_all_event()
    mc_load_all_event()
    miniserver = await aiorak.create_server((host, port), handler, guid=666)
    logger.info(f"Server started at {host}:{port}")
    logger.add(send_log, level="INFO", format="#W[{level}] {message}")

    await miniserver.serve_forever()


def stop():
    for player in players:
        player.kick()
    mn2mc.running = False

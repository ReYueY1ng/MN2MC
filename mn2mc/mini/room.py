import random
import hashlib
import json
import time
import urllib.parse
import asyncio

import aiohttp
from loguru import logger

import mn2mc
import mn2mc.mini
import mn2mc.mini.auth
import mn2mc.mini.nat
import mn2mc.mini.wsconn

CONFIG_URL = " http://openroom.mini1.cn:8080/server/room?"
AUTH_KEY = "f5711eb1640712de051e5aedc35329c3"

CREATE_ROOM_PARAMS = {
    "can_trace": "9323",
    "cmd": "create_room",
    "connect_mode": "1",
    "country": "CN",
    "desc": "",
    "device": "110",
    "extra_data": '{"audioconfigurl":"","autoTag":"创造","editorSceneSwitch":1,"gender":2,"limit":6,"modGoods":[],"modUuids":[],"modurl":"","platform":1,"stime":1777623867,"translate_sourcelang":0,"uilibsurl":"","uniqueCode":"","version":"1.55.0","vipExp":0,"vipLevel":0,"vipType":0,"worldtype":4}',
    "game_label": "3",
    "has_avatar": "1",
    "map_id": "193fdcb882eba37a63b843029f000af1",
    "map_type": "10260950510809",
    "map_version": "0",
    "max_count": "40",
    "net_area": "0",
    "net_isp": "0",
    "net_status": "2",
    "passwd": "",
    "proxy_ip": "",
    "proxy_port": "",
    "punch_ip": "",
    "punch_port": "",
    "right": "1",
    "room_name": "",
    "room_type": "4",
    "s2t": "",
    "thumbnail": "",
    "time": "1777623867",
    "token": "",
    "uicon": "645",
    "uicon_box": "33279",
    "uin": "",
    "uname": "",
    "use_proxy": "0",
    "version": "1.55.0",
}

CREATE_ROOM_EXTEND_PARAMS = {
    "public_type": "0",
    "prei_room_name_idx": "0",
    "regapiid": "6",
    "cltapiid": "110",
    "cltversion": "79616",
    "lang": "0",
    "game_session_id": "",
    "session_id": "",
    "room_token": "",
}

room_url = "http://%s:%s/server/room?"
config = {}
session_id = "".join(random.choices("0123456789abcdef", k=32))
room_token: str
player_count = 0
_update_task: asyncio.Task | None = None


def _make_auth(params: dict) -> str:
    """MD5(sorted non-empty params + AUTH_KEY)."""
    body = "&".join(f"{k}={v}" for k, v in sorted(params.items()) if v is not None)
    return hashlib.md5((body + AUTH_KEY).encode()).hexdigest()


async def get_config():
    global config
    logger.info("Getting server config...")
    config_params = {"cmd": "server_config", "uin": mn2mc.mini.auth.uin}
    encoded_params = urllib.parse.urlencode(config_params)
    encoded_params += (
        "&auth=" + hashlib.md5((encoded_params + AUTH_KEY).encode()).hexdigest()
    )
    async with aiohttp.ClientSession() as session:
        async with session.get(
            CONFIG_URL + encoded_params, headers=mn2mc.mini.HEADERS
        ) as response:
            data = await response.text()
            jsondata = json.loads(data)
            if jsondata["result"] == 0:
                config = jsondata["config"]
                return config
            else:
                raise Exception(f"Failed to get server config: {data}")


async def create_room():
    global room_url, room_token
    server_config = await get_config()
    room_url = room_url % (server_config["room"]["ip"], server_config["room"]["port"])
    logger.info("Creating room...")
    cur_time = str(int(time.time()))
    room_token = f"{mn2mc.mini.auth.uin:0>12}{int(cur_time):0>12}{session_id}"

    params = CREATE_ROOM_PARAMS.copy()
    params["device"] = str(mn2mc.mini.auth.api_id)
    params["extra_data"] = (
        "{"
        f'"audioconfigurl":"","autoTag":"创造","editorSceneSwitch":0,"version":"{mn2mc.mini.version}",'
        #'"limit":6,"modGoods":[],"modUuids":[],"modurl":"","platform":1,'
        #f'"stime":{cur_time},"translate_sourcelang":0,"uilibsurl":"",'
        #f'"uniqueCode":"{room_token}","version":"{mn2mc.mini.version}",'
        '"worldtype":4'
        "}"
    )
    params["proxy_ip"] = server_config["proxy"]["ip"]
    params["proxy_port"] = server_config["proxy"]["port"]
    params["punch_ip"] = server_config["punch"]["ip"]
    params["punch_port"] = server_config["punch"]["port"]
    params["room_name"] = f"MN2MC {mn2mc.version}"
    params["s2t"] = mn2mc.mini.wsconn.s2t
    params["time"] = cur_time
    params["token"] = hashlib.md5(
        (cur_time + mn2mc.mini.wsconn.s2 + str(mn2mc.mini.auth.uin)).encode()
    ).hexdigest()
    params["uin"] = str(mn2mc.mini.auth.uin)
    params["version"] = mn2mc.mini.version

    extend_params = CREATE_ROOM_EXTEND_PARAMS.copy()
    extend_params["session_id"] = session_id
    extend_params["room_token"] = room_token
    extend_params["cltapiid"] = str(mn2mc.mini.auth.api_id)
    extend_params["cltversion"] = str(mn2mc.mini.cltversion)

    encoded = urllib.parse.urlencode(params)
    auth = _make_auth(params)
    encoded += f"&{urllib.parse.urlencode(extend_params)}&auth={auth}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            room_url + encoded, headers=mn2mc.mini.HEADERS
        ) as response:
            data = await response.text()
            jsondata = json.loads(data)
            if jsondata["result"] == 0:
                logger.info("Room created. Now you can search the room by uin.")
                await mn2mc.mini.nat.start()
                _start_update_loop()
            else:
                raise Exception(f"Failed to create room: {data}")



async def room_update(count: int | None = None):
    global player_count
    if count is not None:
        player_count = count
    if not room_token:
        return

    # Auth is computed on first 9 params only
    auth_params = {
        "cmd": "host_update_room",
        "locked": "0",
        "members": str(mn2mc.mini.auth.uin),
        "ping": "89",
        "aiPlayerCounts": "",
        "ready": "1",
        "stage": "0",
        "uin": str(mn2mc.mini.auth.uin),
        "umpire": "0",
    }
    auth = _make_auth(auth_params)

    # Remaining params added to URL but NOT auth
    params = {
        **auth_params,
        "pause": "0",
        "can_trace": "9323",
        "public_type": "0",
        "max_count": "10",
        "passwd": "",
        "is_empty_night": "0",
    }
    encoded = urllib.parse.urlencode(params) + f"&auth={auth}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                room_url + encoded, headers=mn2mc.mini.HEADERS
            ) as response:
                result = json.loads(await response.text())
                if result["result"] != 0:
                    logger.error(f"Room update failed: {result}")
    except Exception as e:
        logger.error(f"Room update failed: {e}")


async def close_room():
    global _update_task
    if _update_task:
        _update_task.cancel()
        _update_task = None
    if not room_token:
        return

    # Auth computed on cmd + uin only
    auth = _make_auth({
        "cmd": "close_room",
        "uin": str(mn2mc.mini.auth.uin),
    })

    params = {
        "cmd": "close_room",
        "uin": str(mn2mc.mini.auth.uin),
        "apiid": str(mn2mc.mini.auth.api_id),
        "country": "CN",
        "lang": "0",
        "ver": mn2mc.mini.version,
        "regapiid": "6",
        "cltapiid": str(mn2mc.mini.auth.api_id),
        "cltversion": str(mn2mc.mini.cltversion),
        "game_session_id": "",
        "session_id": session_id,
        "room_token": room_token,
    }
    encoded = urllib.parse.urlencode(params) + f"&auth={auth}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                room_url + encoded, headers=mn2mc.mini.HEADERS
            ) as response:
                result = json.loads(await response.text())
                if result.get("result") != 0:
                    logger.error(f"Close room failed: {result}")
                else:
                    logger.info("Room closed successfully")
    except Exception as e:
        logger.error(f"Close room failed: {e}")


def _start_update_loop():
    global _update_task

    async def _loop():
        await room_update()
        while True:
            await asyncio.sleep(15)
            await room_update()

    _update_task = asyncio.create_task(_loop())
    logger.info("Room update loop started (every 15s)")


def set_player_count(count: int):
    global player_count
    player_count = count

import random
import hashlib
import json
import time
import urllib.parse
import asyncio
from typing import TYPE_CHECKING

import aiohttp
from loguru import logger

import mn2mc
import mn2mc.mini
import mn2mc.mini.auth
import mn2mc.mini.nat
import mn2mc.mini.wsconn
import mn2mc.config

CONFIG_URL = "http://openroom.mini1.cn:8080/server/room?"
AUTH_KEY = "f5711eb1640712de051e5aedc35329c3"

CREATE_ROOM_PARAMS = {
    "can_trace": "9335",
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
    "version": str(mn2mc.mini.version),
}

CREATE_ROOM_EXTEND_PARAMS = {
    "public_type": "0",
    "prei_room_name_idx": "0",
    "regapiid": "6",
    "cltapiid": "110",
    "cltversion": str(mn2mc.mini.cltversion),
    "lang": "0",
    "game_session_id": "",
    "session_id": "",
    "room_token": "",
}


class MiniRoom:
    """Manages Mini World room creation, updates, and teardown."""

    def __init__(self) -> None:
        self.config: dict = {}
        self.room_token: str = ""
        self.player_count: int = 0
        self.room_url: str = "http://%s:%s/server/room?"
        self.session_id: str = "".join(random.choices("0123456789abcdef", k=32))
        self._update_task: asyncio.Task | None = None

    @staticmethod
    def _make_auth(params: dict) -> str:
        """MD5(sorted non-empty params + AUTH_KEY)."""
        body = "&".join(f"{k}={v}" for k, v in sorted(params.items()) if v is not None)
        return hashlib.md5((body + AUTH_KEY).encode()).hexdigest()

    async def get_config(self) -> dict:
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
                    self.config = jsondata["config"]
                    return self.config
                else:
                    raise Exception(f"Failed to get server config: {data}")

    async def create_room(self) -> None:
        server_config = await self.get_config()
        self.room_url = self.room_url % (server_config["room"]["ip"], server_config["room"]["port"])
        logger.info("Creating room...")
        cur_time = str(int(time.time()))
        self.room_token = f"{mn2mc.mini.auth.uin:0>12}{int(cur_time):0>12}{self.session_id}"

        params = CREATE_ROOM_PARAMS.copy()
        params["device"] = str(mn2mc.mini.auth.api_id)
        params["extra_data"] = (
            "{"
            f'"audioconfigurl":"","autoTag":"创造","editorSceneSwitch":0,"version":"{mn2mc.mini.version}",'
            #'"limit":6,"modGoods":[],"modUuids":[],"modurl":"","platform":1,'
            #f'"stime":{cur_time},"translate_sourcelang":0,"uilibsurl":"",'
            #f'"uniqueCode":"{self.room_token}","version":"{mn2mc.mini.version}",'
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
        extend_params["session_id"] = self.session_id
        extend_params["room_token"] = self.room_token
        extend_params["cltapiid"] = str(mn2mc.mini.auth.api_id)
        extend_params["cltversion"] = str(mn2mc.mini.cltversion)

        encoded = urllib.parse.urlencode(params)
        auth = self._make_auth(params)
        encoded += f"&{urllib.parse.urlencode(extend_params)}&auth={auth}"

        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.room_url + encoded, headers=mn2mc.mini.HEADERS
            ) as response:
                data = await response.text()
                jsondata = json.loads(data)
                if jsondata["result"] == 0:
                    logger.info("Room created. Now you can search the room by uin.")
                    await mn2mc.mini.nat.start()
                    self._start_update_loop()
                else:
                    raise Exception(f"Failed to create room: {data}")

    async def room_update(self, count: int | None = None) -> None:
        if count is not None:
            self.player_count = count
        if not self.room_token:
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
        auth = self._make_auth(auth_params)

        # Remaining params added to URL but NOT auth
        params = {
            **auth_params,
            "pause": "0",
            "can_trace": "9335",
            "public_type": "0",
            "max_count": str(mn2mc.config.mini['server']['max_players']),
            "passwd": "",
            "is_empty_night": "0",
        }
        encoded = urllib.parse.urlencode(params) + f"&auth={auth}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.room_url + encoded, headers=mn2mc.mini.HEADERS
                ) as response:
                    result = json.loads(await response.text())
                    if result["result"] != 0:
                        logger.error(f"Room update failed: {result}")
        except Exception as e:
            logger.error(f"Room update failed: {e}")

    async def close_room(self) -> None:
        if self._update_task:
            self._update_task.cancel()
            self._update_task = None
        if not self.room_token:
            return

        # Auth computed on cmd + uin only
        auth = self._make_auth({
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
            "session_id": self.session_id,
            "room_token": self.room_token,
        }
        encoded = urllib.parse.urlencode(params) + f"&auth={auth}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.room_url + encoded, headers=mn2mc.mini.HEADERS
                ) as response:
                    result = json.loads(await response.text())
                    if result.get("result") != 0:
                        logger.error(f"Close room failed: {result}")
                    else:
                        logger.info("Room closed successfully")
        except Exception as e:
            logger.error(f"Close room failed: {e}")

        await mn2mc.mini.nat.stop()

    def _start_update_loop(self) -> None:
        async def _loop() -> None:
            try:
                await self.room_update()
                while True:
                    await asyncio.sleep(15)
                    await self.room_update()
            except asyncio.CancelledError:
                raise
            except Exception:
                logger.exception("Room update loop crashed")

        self._update_task = asyncio.create_task(_loop())
        logger.info("Room update loop started (every 15s)")

    def set_player_count(self, count: int) -> None:
        self.player_count = count


# Module-level singleton — all external code accesses via mn2mc.mini.room.xxx
room = MiniRoom()

if TYPE_CHECKING:
    config: dict
    room_token: str
    player_count: int
    room_url: str
    session_id: str
    _update_task: asyncio.Task | None
    async def get_config() -> dict: ...
    async def create_room() -> None: ...
    async def room_update(count: int | None = None) -> None: ...
    async def close_room() -> None: ...
    def set_player_count(count: int) -> None: ...


def __getattr__(name: str):
    """Proxy attribute access to the room singleton for backward compatibility.

    This allows `mn2mc.mini.room.room_token`, `mn2mc.mini.room.config`, etc.
    to transparently resolve to `room.room_token`, `room.config`, etc.
    """
    if name in {
        "config", "room_token", "player_count", "room_url",
        "session_id", "_update_task",
        "get_config", "create_room", "room_update", "close_room",
        "_start_update_loop", "set_player_count",
    }:
        return getattr(room, name)
    raise AttributeError(f"module 'mn2mc.mini.room' has no attribute {name!r}")

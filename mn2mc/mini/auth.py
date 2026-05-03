import base64
import hashlib
import json
import time

import aiohttp
import ormsgpack
from loguru import logger

import mn2mc
import mn2mc.config as config
import mn2mc.mini
import mn2mc.utils.xxtea as xxtea

LOGIN_URL = "https://wskacchm.mini1.cn:14130/man_machine/login_v3?msg=%s&sign=%s"
uin = 0
api_id = 110
jwt = ""
full_sign = ""
s2 = ""
s2t = ""
name = "Unknown"


class MiniAuthenticationError(Exception):
    pass


def encode(data):
    return (
        base64.urlsafe_b64encode(xxtea.encrypt_zip(ormsgpack.packb(data)))
        .replace(b"=", b":")
        .decode()
    )


async def login():
    global uin, name, full_sign, s2, jwt, s2t, api_id
    logger.info(f"Logging in {config.mini['auth']['uin']}...")
    server_time = int(time.time())
    msg = encode(
        {
            "source": "client",
            "juhe_auth": "",
            "passwd_auth": '{"passwd":"' + config.mini["auth"]["passwd"] + '"}',
            "DeviceID": config.mini["auth"]["device_id"],
            "is_url": True,
            "geetest": "blending",
            "target": "login",
            "apiid": config.mini["auth"]["api_id"],
            "juhe_strong_auth": "",
            "svrTime": server_time,
            "login_type": "passwd",
            "version": mn2mc.mini.cltversion,
            "time": server_time,
            "uin": config.mini["auth"]["uin"],
        }
    )

    msgsign = hashlib.md5(
        f"msg={msg}&key=2ddb7619717147439c83ab022e9d4d38".encode()
    ).hexdigest()

    async with aiohttp.ClientSession() as session:
        async with session.get(
            LOGIN_URL % (msg, msgsign), headers=mn2mc.mini.HEADERS
        ) as response:
            text = await response.text()
            data = json.loads(text)
            if data["code"] == 0:
                uin = int(config.mini["auth"]["uin"])
                api_id = config.mini["auth"]["api_id"]
                name = data["baseinfo"]["RoleInfo"]["NickName"]
                full_sign = data["authinfo"]["sign"]
                s2, s2t = full_sign.split("_")
                jwt = data["authinfo"]["token"]
                logger.info(f"Login success, name: {name}")
            else:
                raise MiniAuthenticationError(
                    f"Login failed with code {data['code']}: {data['msg']}"
                )

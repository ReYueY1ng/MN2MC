"""
Get s2 (serverData) and s2t from the Mini World WebSocket server.
Connects, sends one heartbeat, extracts sign from response, saves, disconnects.

The WebSocket heartbeat returns a DIFFERENT sign than the HTTP login response.
This is the ACTUAL s2/s2t used by the game (heartbeat value overwrites login value).

Usage (standalone):
    python -m mn2mc.mini.wsconn
"""

import asyncio
import json
import urllib.parse
from datetime import datetime
from typing import TYPE_CHECKING

import aiohttp
import ormsgpack
from loguru import logger
from websockets.asyncio.client import connect

import mn2mc.mini
import mn2mc.mini.auth
import mn2mc.utils.xxtea as xxtea

CONFIG_URL = "http://wskacchm.mini1.cn:4000/update/?"


class WsConnManager:
    """Manages WebSocket connection to Mini World server for s2/s2t retrieval."""

    def __init__(self):
        self.s2: str = ""
        self.s2t: str = ""

    @staticmethod
    def encode(data):
        return xxtea.encrypt(ormsgpack.packb(data))

    @staticmethod
    def decode(data):
        return ormsgpack.unpackb(xxtea.decrypt(data))

    async def get_ws_url(self) -> str:
        config_params = {
            "cltversion": mn2mc.mini.cltversion,
            "clttype": 0,
            "uin": mn2mc.mini.auth.uin,
            "game_env": 0,
            "ver": mn2mc.mini.version,
            "apiid": mn2mc.mini.auth.api_id,
            "lang": 0,
            "country": "CN",
        }
        encoded = urllib.parse.urlencode(config_params)
        async with aiohttp.ClientSession() as session:
            async with session.get(
                CONFIG_URL + encoded, headers=mn2mc.mini.HEADERS
            ) as resp:
                text = await resp.text()
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    raise ValueError(f"Failed to parse WS config response: {text[:200]}")
                logger.info(f"WS URL: {data['conn']}")
                return data["conn"]

    async def fetch_s2(self) -> dict:
        """Connect, send heartbeat, get s2/s2t, disconnect."""
        await mn2mc.mini.auth.login()
        jwt = mn2mc.mini.auth.jwt
        uin = mn2mc.mini.auth.uin

        logger.info("Getting websocket url...")
        ws_url = await self.get_ws_url()
        logger.info("Fetching s2...")
        async with connect(
            ws_url, user_agent_header=mn2mc.mini.HEADERS["User-Agent"]
        ) as ws:
            # Send heartbeat: [0, seq, token]
            seq = int(datetime.now().timestamp() * 1000) % 10000000
            hb = self.encode([0, seq, jwt])
            await ws.send(hb)
            # Wait for response
            raw = await asyncio.wait_for(ws.recv(), timeout=10)
            data = self.decode(raw)
            # Parse: [1, seq, code, result, other]
            if data[0] != 1 or len(data) < 4:
                raise ValueError(f"Unexpected HB response: {data}")
            code = data[2]
            result = data[3]
            if code != 0:
                raise ValueError(f"HB error code={code}")
            if "_" not in str(result):
                raise ValueError(f"Invalid sign format: {result}")
            self.s2, self.s2t = str(result).split("_", 1)
            session = {
                "s2": self.s2,
                "s2t": self.s2t,
                "uin": uin,
                "jwt": jwt,
                "captured_at": datetime.now().isoformat(),
            }
            logger.info("Fetch s2 success!")

            return session

    def save(self, session: dict, path: str = "s2_session.json") -> None:
        with open(path, "w") as f:
            json.dump(session, f, indent=2)
        logger.info(f"Saved to {path}")

    async def main(self):
        session = await self.fetch_s2()
        logger.info(session)
        self.save(session)


# Module-level singleton
wsconn = WsConnManager()

if TYPE_CHECKING:
    s2: str
    s2t: str
    async def fetch_s2() -> dict: ...
    def save(session: dict, path: str = ...) -> None: ...


def __getattr__(name):
    """Proxy attribute access to the wsconn singleton for backward compatibility."""
    if hasattr(wsconn, name):
        return getattr(wsconn, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


if __name__ == "__main__":
    asyncio.run(wsconn.main())

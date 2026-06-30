import asyncio
import atexit

import mn2mc.config as config
import mn2mc.mini.auth
import mn2mc.mini.room

_process: asyncio.subprocess.Process | None = None


def _cleanup():
    global _process
    if _process is not None:
        try:
            _process.terminate()
        except Exception:
            pass
        _process = None


atexit.register(_cleanup)


async def start():
    global _process
    _process = await asyncio.create_subprocess_exec(
        "./tools/raknet_proxy",
        "-target_ip",
        "127.0.0.1",
        "-target_port",
        str(config.mini["server"]["port"]),
        "-nat_ip",
        mn2mc.mini.room.config["punch"]["ip"],
        "-nat_port",
        str(mn2mc.mini.room.config["punch"]["port"]),
        "-guid",
        hex(mn2mc.mini.auth.uin)[2:],
        "-coordinator_ip",
        mn2mc.mini.room.config["proxy"]["ip"],
        "-coordinator_port",
        str(mn2mc.mini.room.config["proxy"]["port"]),
        "-upnp",
        "-max_clients",
        str(mn2mc.config.mini['server']['max_players']),
        start_new_session=True
    )


async def stop():
    global _process
    if _process is not None:
        _process.terminate()
        await _process.wait()
        _process = None

import importlib
import struct
import types
from typing import Optional

from loguru import logger

PLACEHOLDER = b"\x90\x00\x02\x9a"

events = {}


class MiniClientPacket:
    uin: int
    msgcode: int
    data: bytes

    def __init__(self, uinordata: int | bytes | None, msgcode: Optional[int] = None, data: Optional[bytes] = None) -> None:
        if type(uinordata) is int:
            if type(msgcode) is not int:
                raise TypeError('msgcode must be int')
            elif type(data) is not bytes:
                raise TypeError('data must be bytes')
            self.uin = uinordata
            self.msgcode = msgcode
            self.data = data
        elif type(uinordata) is bytes:
            self.decode(uinordata)
    def __str__(self) -> str:
        return f"""\
Uin: {self.uin}
MsgCode: {self.msgcode}
data: {self.data}
"""

    def decode(self, data: bytes) -> None:
        self.uin = struct.unpack(">I", data[1:5])[0]
        self.msgcode, length = struct.unpack("<HH", data[9:13])
        self.data = struct.unpack_from(f"{length}s", data, 13)[0]

    def encode(self) -> bytes:
        return (
            b"\x89"
            + struct.pack(">I", self.uin)
            + PLACEHOLDER
            + struct.pack("<HH", self.msgcode, len(self.data))
            + self.data
        )


class MiniServerPacket:
    msgcode: int
    data: bytes = b""

    def __init__(self, msgcode: Optional[int], data: Optional[bytes]) -> None:
        if msgcode:
            self.msgcode = msgcode
        if data:
            self.data = data

    def __str__(self) -> str:
        return f"""\
MsgCode: {self.msgcode}
data: {self.data}
"""

    def decode(self, data: bytes) -> None:
        self.msgcode, length = struct.unpack("<HH", data[1:5])
        self.data = struct.unpack_from(f"{length}s", data, 5)[0]

    def encode(self) -> bytes:
        return b"\x89" + struct.pack("<HH", self.msgcode, len(self.data)) + self.data


def add_event(event: int, func: types.FunctionType):
    __check_event(event)
    events[event].append(func)
    return len(events[event])


def del_event(event: int, id: int):
    __check_event(event)
    events[event][id] = None


def reset_events():
    global events
    events = {}


def __check_event(event: int):
    if event not in events:
        events[event] = []


async def on_event(event: int, player: object, mcp: MiniClientPacket):
    __check_event(event)
    for func in events[event]:
        try:
            await func(player, mcp)
        except Exception as e:
            logger.exception(f"Exception occurred: {str(e)}")


def load_all_event():
    importlib.import_module("mn2mc.mini.packetevents")

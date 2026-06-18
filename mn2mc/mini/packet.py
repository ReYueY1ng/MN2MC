import importlib
import struct
from typing import Optional

from mn2mc.events import add_event, del_event, on_event, reset_events

PLACEHOLDER = b"\x90\x00\x02\x9a"


class MiniClientPacket:
    """Packet received from a Mini World client.

    Format: \\x89 + 4-byte big-endian uin + 8-byte placeholder + 2-byte LE msgcode + 2-byte LE length + data
    """

    uin: int
    msgcode: int
    data: bytes

    def __init__(self, uinordata: int | bytes | None, msgcode: Optional[int] = None, data: Optional[bytes] = None) -> None:
        if isinstance(uinordata, int):
            if not isinstance(msgcode, int):
                raise TypeError('msgcode must be int')
            elif not isinstance(data, bytes):
                raise TypeError('data must be bytes')
            self.uin = uinordata
            self.msgcode = msgcode
            self.data = data
        elif isinstance(uinordata, bytes):
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
    """Packet sent from the proxy server to a Mini World client.

    Format: \\x89 + 2-byte LE msgcode + 2-byte LE length + data
    """

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


def load_all_event():
    """Import all Mini World packet event handlers from the packetevents module."""
    importlib.import_module("mn2mc.mini.packetevents")

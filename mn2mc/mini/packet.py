import importlib
import struct
from typing import Optional

from mn2mc.events import add_event, del_event, on_event, reset_events

PLACEHOLDER = b"\x90\x00\x02\x9a"


class MiniClientPacket:
    """Packet received from a Mini World client.

    Format: \\x89 + 4-byte big-endian uin + 4-byte big-endian uin + 2-byte LE msgcode + 2-byte LE length + data
    """

    uin: int
    msgcode: int
    data: bytes
    touin: int

    def __init__(
        self,
        uinordata: int | bytes | None,
        msgcode: Optional[int] = None,
        data: Optional[bytes] = None,
        touin: Optional[int] = None,
    ) -> None:
        if isinstance(uinordata, int):
            if not isinstance(msgcode, int):
                raise TypeError("msgcode must be int")
            elif not isinstance(data, bytes):
                raise TypeError("data must be bytes")
            elif not isinstance(touin, int):
                raise TypeError("touin must be int")
            self.uin = uinordata
            self.msgcode = msgcode
            self.data = data
            self.touin = touin
        elif isinstance(uinordata, bytes):
            self.decode(uinordata)

    def __str__(self) -> str:
        return f"""\
Uin: {self.uin}
MsgCode: {self.msgcode}
data: {self.data}
touin: {self.touin}
"""

    def decode(self, data: bytes) -> None:
        self.uin = struct.unpack(">I", data[1:5])[0]
        self.touin = struct.unpack(">I", data[5:9])[0]
        self.msgcode, length = struct.unpack("<HH", data[9:13])
        self.data = struct.unpack_from(f"{length}s", data, 13)[0]

    def encode(self) -> bytes:
        return (
            b"\x89"
            + struct.pack(">I", self.uin)
            + struct.pack(">I", self.touin)
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
        if msgcode is not None:
            self.msgcode = msgcode
        if data is not None:
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

import aiorak
from loguru import logger

import mn2mc.config as config
import mn2mc.mini.auth
import mn2mc.mini.proto as proto
import mn2mc.utils.protobuf_parser as protobuf_parser
from mn2mc.mc.client import MCClient
from mn2mc.mini.packet import MiniClientPacket, MiniServerPacket, on_event
from mn2mc.mini.proto import common

players = []


class MiniPlayer:
    """Represents a connected Mini World client player.

    Manages the RakNet connection, packet sending, and lifecycle
    of a Mini World client connected through the proxy.
    """

    uin: int = 0
    name: str = "Unknown"
    conn: aiorak.Connection
    mcclient: MCClient
    cltversion: int

    def __init__(self, conn: aiorak.Connection, uin: int) -> None:
        self.conn = conn
        self.uin = uin
        players.append(self)

    def __del__(self) -> None:
        if self.conn.state == aiorak.ConnectionState.CONNECTED:
            self.kick()
        if hasattr(self, "mcclient"):
            self.mcclient.running = False
            self.mcclient.end()
            self.mcclient.remove()

    def __repr__(self) -> str:
        return f"<MiniPlayer {self.name} ({self.uin}): {self.conn}>"

    def send_packet(
        self,
        msg_code: int,
        data: bytes,
        reliability: aiorak.Reliability = aiorak.Reliability.RELIABLE_ORDERED,
        priority: aiorak.Priority = aiorak.Priority.MEDIUM,
    ) -> None:
        """Send a packet to the Mini World client."""
        # logger.debug(f"({self.uin}) send packet {msg_code}")
        if self.conn.state == aiorak.ConnectionState.CONNECTED:
            if config.mini["server"]["host_to_room_server"]:
                self.conn.send(
                    MiniClientPacket(mn2mc.mini.auth.uin, msg_code, data).encode(),
                    reliability,
                    priority=priority,
                )
            else:
                self.conn.send(
                    MiniServerPacket(msg_code, data).encode(),
                    reliability,
                    priority=priority,
                )

    def send_msg(self, msg: str, nocolor: bool = False):
        """Send a system chat message to the Mini World client."""
        self.send_packet(
            common.ePBMsgCode.PB_CHAT_HC,
            proto.hc.PB_ChatHC(
                ChatType=1, Content=msg if nocolor else "#W" + msg
            ).SerializeToString(),
            priority=aiorak.Priority.IMMEDIATE,
        )

    def send_player_msg(
        self, uin: int = 0, speaker: str = "System", msg: str = "default"
    ):
        """Send a player chat message to the Mini World client."""
        self.send_packet(
            common.ePBMsgCode.PB_CHAT_HC,
            proto.hc.PB_ChatHC(
                ChatType=0, Uin=uin, Speaker=speaker, Content=msg
            ).SerializeToString(),
        )

    def kick(self) -> None:
        """Disconnect the Mini World client and clean up resources."""
        if self.conn.state == aiorak.ConnectionState.CONNECTED:
            self.conn.disconnect()
        if hasattr(self, "mcclient"):
            self.mcclient.running = False
            self.mcclient.end()
        players.remove(self)

    async def handler(self) -> None:
        """Main packet handling loop for the Mini World client connection."""
        try:
            async for data in self.conn:
                mcp = MiniClientPacket(data)
                if config.debug:
                    protobuf_parser.parse(mcp.msgcode, mcp.data)
                await on_event(mcp.msgcode, self, mcp)
                # logger.debug(mcp)
        except Exception as e:
            logger.exception(f"({self.uin}) Fatal exception occurred: {str(e)}")
            self.kick()

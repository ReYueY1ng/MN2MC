from __future__ import annotations

import json
import threading
import time
import zlib
from typing import TYPE_CHECKING, cast

import aiorak
import javascript
import minebase
import ormsgpack
from javascript import require
from loguru import logger

import mn2mc.config as config
import mn2mc.utils.color_converter as color_converter
from mn2mc.mc.chunk_bridge import MCChunkBridge
from mn2mc.mc.connection import MCConnection
from mn2mc.mc.entity import MCEntity
from mn2mc.mc.entity_tracker import MCEntityTracker
from mn2mc.mc.inventory import MCInventory
from mn2mc.mc.packet import events, on_event
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f

if TYPE_CHECKING:
    from mn2mc.mini.player import MiniPlayer

prismarinechat = require("prismarine-chat")(config.mc.version)
minedata = minebase.load_version(config.mc.version)
language = minedata["language"]
mcprotocol = require("minecraft-protocol")
vec3 = require("vec3")
ChunkManager = require("./chunk.js")
registry = require("prismarine-registry")

# protodef 的数组大小保护(count > 0xffffff)在畸形/错位 NBT 下会抛普通 Error,
# 而不是 PartialReadError. minecraft-protocol 的 FullPacketParser 会把它当作致命
# 错误 cb(e), 销毁整个解析流导致断线. 这里给编译协议打补丁: 每次解析前开启
# noArraySizeCheck, 让同样的越界变成 PartialReadError, 只丢弃那一个包、流继续.
# 补丁作用于原型, 与模块加载顺序无关, 幂等, 覆盖所有状态/连接/重连.
# 注意: eval_js 会把调用帧的局部变量注入 eval 作用域, 所以必须在没有名为 require
# 的局部变量的函数内执行, 否则 Node 的 require 会被模块级的 Python require 遮蔽.
def _patch_protodef_array_guard():
    javascript.eval_js("""
        const { CompiledProtodef } = require('protodef/src/compiler')
        const origParsePacketBuffer = CompiledProtodef.prototype.parsePacketBuffer
        CompiledProtodef.prototype.parsePacketBuffer = function (type, buffer, offset) {
            this.setVariable('noArraySizeCheck', true)
            return origParsePacketBuffer.call(this, type, buffer, offset)
        }
    """)

try:
    _patch_protodef_array_guard()
except Exception:
    logger.exception("Failed to patch CompiledProtodef.parsePacketBuffer")


class MCClient:
    MAX_PENDING_ITEMS = 1000
    miniplayer: MiniPlayer
    on_events: list[str]
    username: str
    _username_candidates: list[str]
    _username_index: int
    _base_options: dict

    def __init__(
        self,
        options: dict,
        miniplayer: MiniPlayer,
        _username_candidates: list[str] | None = None,
    ) -> None:
        self._username_candidates = _username_candidates or []
        self._username_index = 0
        self._base_options = options
        self.username = options["username"]
        self.miniplayer = miniplayer
        self.on_events: list[str] = []

        # Create component instances
        self._inventory = MCInventory()
        self._entity_tracker = MCEntityTracker()
        self._connection: MCConnection = cast(MCConnection, None)  # set in _setup_connection
        self._chunk_bridge: MCChunkBridge | None = None

        logger.info(
            f"({miniplayer.name}) Connecting to {options['host']}:{options['port']}"
        )
        self._setup_connection(options)

    def _setup_connection(self, options: dict) -> None:
        """Create MC client connection and bind event handlers."""
        if self._chunk_bridge is not None:
            self._chunk_bridge.stop()
            self._chunk_bridge = None
        self.client = mcprotocol.createClient(options)

        # Create/reset connection component
        self._connection = MCConnection(self.client, self.miniplayer)
        self._connection.registry = registry(config.mc.version)

        # Reset other components
        self._entity_tracker.reset()
        self._inventory.reset()

        self.client.on("error", self.on_error)
        self.client.on("end", self.on_end)
        self.client.on("disconnect", self.on_disconnect)
        self.client.on("connect", self.on_connect)
        self.on_events = []
        self.client.on("playerChat", self.on_player_chat)
        self.client.on("systemChat", self.on_server_chat)
        self.client.on("state", self.on_state_change)
        self.load_events()
        if config.mc.use_new_chunk_parser:
            self._chunk_bridge = MCChunkBridge(self, self.client, self.registry)
            self._chunk_bridge.start(self.miniplayer.name, self.running)
        else:
            javascript.eval_js("""
                self.client.on("registry_data", (data) => {
                    if (data.id == "minecraft:dimension_type") self.registry.loadDimensionCodec(data)
                })
            """)

    # ==================================================================
    # Backward-compatible delegation: connection component
    # ==================================================================

    @property
    def state(self) -> str:
        return self._connection.state

    @state.setter
    def state(self, value: str) -> None:
        self._connection.state = value

    @property
    def _connected(self) -> bool:
        return self._connection._connected

    @_connected.setter
    def _connected(self, value: bool) -> None:
        self._connection._connected = value

    @property
    def running(self):
        return self._connection.running

    @property
    def position(self) -> Vector3f:
        return self._connection.position

    @position.setter
    def position(self, value: Vector3f) -> None:
        self._connection.position = value

    @property
    def angle(self) -> Angle:
        return self._connection.angle

    @angle.setter
    def angle(self, value: Angle) -> None:
        self._connection.angle = value

    @property
    def registry(self):
        return self._connection.registry

    @registry.setter
    def registry(self, value):
        self._connection.registry = value

    @property
    def _dimension(self) -> int:
        return self._connection._dimension

    @_dimension.setter
    def _dimension(self, value: int) -> None:
        self._connection._dimension = value

    @property
    def dimension(self) -> int:
        return self._connection.dimension

    @dimension.setter
    def dimension(self, value: int) -> None:
        self._connection.dimension = value

    @property
    def on_ground(self) -> bool:
        return self._connection.on_ground

    @on_ground.setter
    def on_ground(self, value: bool) -> None:
        self._connection.on_ground = value

    @property
    def sneaking(self) -> bool:
        return self._connection.sneaking

    @sneaking.setter
    def sneaking(self, value: bool) -> None:
        self._connection.sneaking = value

    # ==================================================================
    # Backward-compatible delegation: entity tracker component
    # ==================================================================

    @property
    def entities(self) -> dict[int, MCEntity]:
        return self._entity_tracker.entities

    @entities.setter
    def entities(self, value: dict[int, MCEntity]) -> None:
        self._entity_tracker.entities = value

    @property
    def players(self) -> dict:
        return self._entity_tracker.players

    @players.setter
    def players(self, value: dict) -> None:
        self._entity_tracker.players = value

    @property
    def entityid(self) -> int:
        return self._entity_tracker.entityid

    @entityid.setter
    def entityid(self, value: int) -> None:
        self._entity_tracker.entityid = value

    @property
    def add_player_count(self) -> int:
        return self._entity_tracker.add_player_count

    @add_player_count.setter
    def add_player_count(self, value: int) -> None:
        self._entity_tracker.add_player_count = value

    # ==================================================================
    # Backward-compatible delegation: inventory component
    # ==================================================================

    @property
    def window_id(self) -> int:
        return self._inventory.window_id

    @window_id.setter
    def window_id(self, value: int) -> None:
        self._inventory.window_id = value

    @property
    def inventory_type(self) -> str | int:
        return self._inventory.inventory_type

    @inventory_type.setter
    def inventory_type(self, value: str | int) -> None:
        self._inventory.inventory_type = value

    @property
    def container_sequence(self) -> int:
        return self._inventory.container_sequence

    @container_sequence.setter
    def container_sequence(self, value: int) -> None:
        self._inventory.container_sequence = value

    @property
    def block_sequence(self) -> int:
        return self._inventory.block_sequence

    @block_sequence.setter
    def block_sequence(self, value: int) -> None:
        self._inventory.block_sequence = value

    @property
    def container_ts(self) -> float:
        return self._inventory.container_ts

    @container_ts.setter
    def container_ts(self, value: float) -> None:
        self._inventory.container_ts = value

    @property
    def _open_pending(self) -> bool:
        return self._inventory._open_pending

    @_open_pending.setter
    def _open_pending(self, value: bool) -> None:
        self._inventory._open_pending = value

    @property
    def _pending_grids(self) -> int:
        return self._inventory._pending_grids

    @_pending_grids.setter
    def _pending_grids(self, value: int) -> None:
        self._inventory._pending_grids = value

    @property
    def _pending_item_packets(self) -> list[tuple[int, bytes]]:
        return self._inventory._pending_item_packets

    @_pending_item_packets.setter
    def _pending_item_packets(self, value: list[tuple[int, bytes]]) -> None:
        self._inventory._pending_item_packets = value

    @property
    def _open_timer(self) -> threading.Timer | None:
        return self._inventory._open_timer

    @_open_timer.setter
    def _open_timer(self, value: threading.Timer | None) -> None:
        self._inventory._open_timer = value

    @property
    def _lock(self) -> threading.Lock:
        return self._inventory._lock

    # ==================================================================
    # Delegation: chunk bridge
    # ==================================================================

    @property
    def chunkmgr(self):
        if self._chunk_bridge is not None:
            return self._chunk_bridge.chunkmgr
        return None

    @chunkmgr.setter
    def chunkmgr(self, value):
        # Only used during _setup_connection; chunk_bridge holds it
        pass

    # ==================================================================
    # Delegate methods to connection component
    # ==================================================================

    def send(self, name: str, message: dict, ignorestate=False):
        self._connection.send(name, message, ignorestate)

    def chat(self, content: str, ignorestate=False):
        self._connection.chat(content, ignorestate)

    def end(self):
        self._connection.end()

    # ==================================================================
    # Delegate methods to entity tracker
    # ==================================================================

    def resolve_objid(self, entityid: int) -> int | None:
        """Resolve MC entity ID to Mini World objid.

        Returns:
            int: The corresponding Mini World objid
            None: Entity is unknown/tracked (caller should ignore)
        """
        return self._entity_tracker.resolve_objid(self, entityid)

    # ==================================================================
    # MCClient-owned methods (chat handlers, event loading, etc.)
    # ==================================================================

    def on_disconnect(self, packet, _):
        logger.debug(packet)
        logger.warning(
            f"({self.miniplayer.name}) Disconnected from server: {packet['reason']}"
        )
        if not self._connected and self._username_index < len(self._username_candidates):
            next_username = self._username_candidates[self._username_index]
            self._username_index += 1
            logger.info(
                f"({self.miniplayer.name}) MC login rejected, retrying with username: {next_username}"
            )
            self._setup_connection({**self._base_options, "username": next_username})
            return

    def on_end(self, end):
        self.running.clear()
        with self._lock:
            self._pending_item_packets.clear()
        if self.miniplayer.conn.state == aiorak.ConnectionState.CONNECTED:
            logger.info(f"({self.miniplayer.name}) Connection lost: {end}")
            self.miniplayer.kick()

    def on_error(self, err):
        logger.error(f"({self.miniplayer.name}) Error occurred: {err}")

    def on_connect(self):
        self._connected = True
        self.miniplayer.send_msg("Connected to server")

    def on_player_chat(self, e):
        try:
            if "formattedMessage" in e:
                content = json.loads(e["formattedMessage"])
            elif "unsignedContent" in e and e["unsignedContent"]:
                content = json.loads(e["unsignedContent"])
            elif "plainMessage" in e:
                content = {"text": e["plainMessage"]}
            else:
                logger.error("Cannot find available content!")
                logger.debug(e)
                return
        except json.JSONDecodeError:
            logger.exception(f"({self.miniplayer.name}) Failed to parse chat content")
            return
        chat = prismarinechat(content)
        msg = color_converter.convert_minecraft_to_miniworld(chat.toMotd())
        try:
            name = json.loads(e["senderName"])["text"]
        except Exception:
            name = e["senderName"][1:-1]
        if config.mc.log_message:
            logger.debug(f"[Chat] <{name}> {chat.toAnsi()}")
        match e["type"]["chatType"]:
            case 0:  # normal
                from mn2mc.mini.player import get_players_snapshot

                uin = 0
                for player in get_players_snapshot():
                    if player.name == name:
                        uin = player.uin
                        break
                self.miniplayer.send_player_msg(uin, name, msg)
            case 1:  # me
                self.miniplayer.send_msg(f"* {name} {msg}")
            case 2:  # ... whisper to you
                self.miniplayer.send_msg(
                    "#cAAAAAA"
                    + language["commands.message.display.incoming"] % (name, msg)
                )
            case 3:  # You whisper to ...
                self.miniplayer.send_msg(
                    "#cAAAAAA"
                    + language["commands.message.display.outgoing"] % (name, msg)
                )
            case 5:  # say
                self.miniplayer.send_msg(f"[{name}] {msg}")

    def on_server_chat(self, e):
        try:
            chatjson = json.loads(e["formattedMessage"])
        except json.JSONDecodeError:
            logger.exception(f"({self.miniplayer.name}) Failed to parse server chat")
            return
        chat = prismarinechat(chatjson)
        for msg in color_converter.convert_minecraft_to_miniworld(chat.toMotd()).split(
            "\n"
        ):
            self.miniplayer.send_msg(msg)
        if config.mc.log_message:
            logger.debug(f"[Chat] {chat.toAnsi()}")

    def on_state_change(self, newstate, oldstate):
        self.state = newstate
        logger.info(f"({self.miniplayer.name}) state {oldstate} -> {newstate}")

    def on_packet(self, jsondata: dict, metadata: dict, buffer=None, fullbuffer=None):
        # logger.debug(f"mcpacket: {metadata}\n{jsondata}")
        on_event(metadata["name"], self, jsondata, metadata)

    def remove(self):
        if self._open_timer is not None:
            self._open_timer.cancel()
            self._open_timer = None
        if self._chunk_bridge is not None:
            self._chunk_bridge.stop()
            self._chunk_bridge = None
        self.end()

    def get_chunks(self):
        cm = self.chunkmgr
        if cm is not None and self.running.is_set() and cm.cacheParsedChunks.length > 0:
            compressed_chunks = cm.compressedChunks.blobValueOf()
            chunks = ormsgpack.unpackb(zlib.decompress(compressed_chunks))
            self.on_packet(chunks, {"name": "parsed_chunk"})

    def get_chunks_task(self):
        while self.running.is_set():
            time.sleep(0.2)
            self.get_chunks()

    def load_events(self):
        # chunk.js owns update_light when the new chunk parser is active: its
        # handler adds the _secY remap Python needs, then forwards via
        # on_packet. Registering 'update_light' here too would make
        # minecraft-protocol dispatch every packet twice — once direct (no
        # _secY → no-op) plus once via the chunk.js forwarding.
        chunk_handled = {"update_light"} if config.mc.use_new_chunk_parser else set()
        for event in events:
            if isinstance(event, str) and event not in self.on_events and event not in chunk_handled:
                self.client.on(event, self.on_packet)
                self.on_events.append(event)

    def set_world_miny(self, miny: int):
        self._connection.set_world_miny(miny)

    def set_world_height(self, height: int):
        self._connection.set_world_height(height)

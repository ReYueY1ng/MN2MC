from __future__ import annotations

import json
import threading
import time
import zlib
from typing import TYPE_CHECKING

import aiorak
import javascript
import minebase
import ormsgpack
from javascript import require
from loguru import logger

import mn2mc.config as config
import mn2mc.utils.color_converter as color_converter
from mn2mc.constants import DIMENSION_OVERWORLD
from mn2mc.mc.entity import MCEntity
from mn2mc.mc.packet import events, on_event
from mn2mc.utils.angle import Angle
from mn2mc.utils.vector import Vector3f

if TYPE_CHECKING:
    from mn2mc.mini.player import MiniPlayer

prismarinechat = require("prismarine-chat")(config.mc["version"])
minedata = minebase.load_version(config.mc["version"])
language = minedata["language"]
mcprotocol = require("minecraft-protocol")
vec3 = require("vec3")
ChunkManager = require("./chunk.js")
registry = require("prismarine-registry")


class MCClient:
    MAX_PENDING_ITEMS = 1000
    _dimension: int
    client: mcprotocol.Client
    miniplayer: MiniPlayer
    on_events: list[str]
    position: Vector3f
    angle: Angle
    username: str
    chunkmgr: ChunkManager
    block_sequence: int
    container_sequence: int
    window_id: int
    inventory_type: str | int
    players: dict
    add_player_count: int
    entities: dict[int, MCEntity]
    registry: registry
    entityid: int
    container_ts: float
    _open_pending: bool
    _pending_grids: int
    _pending_item_packets: list[tuple[int, bytes]]
    _open_timer: threading.Timer | None
    _lock: threading.Lock
    _connected: bool
    _username_candidates: list[str]
    _username_index: int
    _base_options: dict

    def __init__(
        self,
        options: dict,
        miniplayer: MiniPlayer,
        _username_candidates: list[str] | None = None,
    ) -> None:
        self._lock = threading.Lock()
        self.running = threading.Event()
        self.running.set()
        self._connected = False
        self._username_candidates = _username_candidates or []
        self._username_index = 0
        self._base_options = options
        self.username = options["username"]
        self.miniplayer = miniplayer
        self.state = "handshaking"
        self.position = Vector3f()
        self.angle = Angle(0, 0)
        self.block_sequence = 0
        self.container_sequence = 0
        self.inventory_type = "inventory"
        self.window_id = 0
        self.players = {}
        self.add_player_count = 0
        self.entityid = 0
        self.container_ts = 0.0
        self._open_pending = False
        self._pending_grids = 0
        self._pending_item_packets = []
        self._open_timer = None
        self.entities = {}
        self.registry = registry(config.mc["version"])
        self._dimension = DIMENSION_OVERWORLD
        logger.info(
            f"({miniplayer.name}) Connecting to {options['host']}:{options['port']}"
        )
        self._setup_connection(options)

    def _setup_connection(self, options: dict) -> None:
        """Create MC client connection and bind event handlers."""
        self.client = mcprotocol.createClient(options)
        self.client.on("error", self.on_error)
        self.client.on("end", self.on_end)
        self.client.on("disconnect", self.on_disconnect)
        self.client.on("connect", self.on_connect)
        self.on_events = []
        self.position = Vector3f()
        self.angle = Angle(0, 0)
        self.block_sequence = 0
        self.container_sequence = 0
        self.inventory_type = "inventory"
        self.window_id = 0
        self.players = {}
        self.add_player_count = 0
        self.entityid = 0
        self.container_ts = 0.0
        self._open_pending = False
        self._pending_grids = 0
        self._pending_item_packets = []
        self._open_timer = None
        self.entities = {}
        self.registry = registry(config.mc["version"])
        self._dimension = DIMENSION_OVERWORLD
        self.client.on("playerChat", self.on_player_chat)
        self.client.on("systemChat", self.on_server_chat)
        self.client.on("state", self.on_state_change)
        self.load_events()
        if config.mc["use_new_chunk_parser"]:
            self.chunkmgr = ChunkManager(config.mc["version"], self, self.client, self.registry)
            self.get_chunk_thread = threading.Thread(
                target=self.get_chunks_task,
                name=f"({self.miniplayer.name}) Get chunk thread",
                daemon=True,
            )
            self.get_chunk_thread.start()
        else:
            javascript.eval_js("""
                self.client.on("registry_data", (data) => {
                    if (data.id == "minecraft:dimension_type") self.registry.loadDimensionCodec(data)
                })
            """)


    def on_disconnect(self, packet, _):
        logger.debug(packet)
        logger.warning(
            f"({self.miniplayer.name}) Disconnected from server: {packet['reason']}"
        )

    def on_end(self, end):
        if not self._connected and self._username_index < len(self._username_candidates):
            next_username = self._username_candidates[self._username_index]
            self._username_index += 1
            logger.info(
                f"({self.miniplayer.name}) MC login rejected, retrying with username: {next_username}"
            )
            self._setup_connection({**self._base_options, "username": next_username})
            return
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
        if config.mc['log_message']:
            logger.debug(f"[Chat] {chat.toAnsi()}")
        msg = color_converter.convert_minecraft_to_miniworld(chat.toMotd())
        try:
            name = json.loads(e["senderName"])["text"]
        except Exception:
            name = e["senderName"][1:-1]
        match e["type"]["chatType"]:
            case 0:  # normal
                from mn2mc.mini.player import players

                uin = 0
                for player in players.copy():
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
        if config.mc['log_message']:
            logger.debug(f"[Chat] {chat.toAnsi()}")

    def on_state_change(self, newstate, oldstate):
        self.state = newstate
        logger.info(f"({self.miniplayer.name}) state {oldstate} -> {newstate}")

    def on_packet(self, jsondata: dict, metadata: dict, buffer=None, fullbuffer=None):
        # logger.debug(f"mcpacket: {metadata}\n{jsondata}")
        on_event(metadata["name"], self, jsondata, metadata)

    def end(self):
        self.client.end()

    def remove(self):
        if self._open_timer:
            self._open_timer.cancel()
            self._open_timer = None
        if hasattr(self, "chunkmgr"):
            self.chunkmgr.running = False
        self.end()

    def chat(self, content: str, ignorestate=False):
        if self.state == "play" or ignorestate:
            self.client.chat(content)

    def send(self, name: str, message: dict, ignorestate=False):
        if self.state == "play" or ignorestate:
            self.client.write(name, message)

    def get_chunks(self):
        if self.running.is_set() and self.chunkmgr.cacheParsedChunks.length > 0:
            compressed_chunks = self.chunkmgr.compressedChunks.blobValueOf()
            chunks = ormsgpack.unpackb(zlib.decompress(compressed_chunks))
            self.on_packet(chunks, {"name": "parsed_chunk"})

    def get_chunks_task(self):
        while self.running.is_set():
            time.sleep(0.2)
            self.get_chunks()

    def load_events(self):
        for event in events:
            if isinstance(event, str) and event not in self.on_events:
                self.client.on(event, self.on_packet)
                self.on_events.append(event)

    def set_world_miny(self, miny: int):
        if not config.mc["use_new_chunk_parser"]:
            import mn2mc.mc.packetevents.chunk.map_chunk as map_chunk

            map_chunk.miny = miny

    def set_world_height(self, height: int):
        if not config.mc["use_new_chunk_parser"]:
            import mn2mc.mc.packetevents.chunk.map_chunk as map_chunk

            map_chunk.worldheight = height

    @property
    def dimension(self) -> int:
        return self._dimension

    @dimension.setter
    def dimension(self, value: int):
        self._dimension = value
        if not hasattr(self.registry, 'dimensionsById') or self.registry.dimensionsById is None:
            return
        dimdata = self.registry.dimensionsById[value]
        if dimdata is None:
            return
        logger.debug(f"({self.miniplayer.name}) dimension change {dimdata}")
        self.set_world_miny(dimdata.minY)
        self.set_world_height(dimdata.height)

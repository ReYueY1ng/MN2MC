from __future__ import annotations
import time

import zlib
import ormsgpack
import threading

import json

import aiorak
import minebase
from javascript import require
from loguru import logger

import mn2mc.config as config
import mn2mc.utils.color_converter as color_converter
from mn2mc.mc.packet import on_event, events
from mn2mc.utils.vector import Vector3f
from mn2mc.utils.angle import Angle

try:
    from mn2mc.mini.player import MiniPlayer
except Exception:
    pass

prismarinechat = require("prismarine-chat")(config.mc["version"])
minedata = minebase.load_version(config.mc["version"])
language = minedata["language"]
mcprotocol = require("minecraft-protocol")
vec3 = require("vec3")
ChunkManager = require("./chunk.js")


class MCClient:
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
    entities: dict

    def __init__(self, options: dict, miniplayer: MiniPlayer) -> None:
        self.client = mcprotocol.createClient(options)
        self.client.on("error", self.on_error)
        self.username = options["username"]
        self.miniplayer = miniplayer
        self.on_events = []
        self.position = Vector3f()
        self.angle = Angle(0, 0)
        self.block_sequence = 0
        self.container_sequence = 0
        self.inventory_type = "inventory"
        self.window_id = 0
        self.running = True
        self.players = {}
        self.add_player_count = 0
        self.entities = {}
        logger.info(
            f"({miniplayer.name}) Connecting to {options['host']}:{options['port']}"
        )
        self.client.on("end", self.on_end)
        self.client.on("disconnect", self.on_disconnect)
        self.client.on("connect", self.on_connect)
        self.client.on("playerChat", self.on_player_chat)
        self.client.on("systemChat", self.on_server_chat)
        # self.client.on("packet", self.on_packet)
        self.load_events()
        if config.mc["use_new_chunk_parser"]:
            self.chunkmgr = ChunkManager(config.mc["version"], self, self.client)
            self.get_chunk_thread = threading.Thread(
                target=self.get_chunks_task,
                name=f"({self.miniplayer.name}) Get chunk thread",
            )
            self.get_chunk_thread.start()

    def on_disconnect(self, packet, a):
        logger.debug(packet)
        logger.debug(a)
        logger.warning(
            f"({self.miniplayer.name}) Disconnected from server: {packet.reason}"
        )

    def on_end(self, end):
        self.running = False
        if self.miniplayer.conn.state == aiorak.ConnectionState.CONNECTED:
            logger.info(f"({self.miniplayer.name}) Connection lost: {end}")

    def on_error(self, err):
        logger.error(f"({self.miniplayer.name}) Error occurred: {err}")

    def on_connect(self):
        self.miniplayer.send_msg("Connected to server")

    def on_player_chat(self, e):
        logger.debug(e)
        if "formattedMessage" in e:
            content = json.loads(e["formattedMessage"])
        elif "unsignedContent" in e and e["unsignedContent"]:
            content = json.loads(e["unsignedContent"])
        elif "plainMessage" in e:
            content = {"text": e["plainMessage"]}
        else:
            logger.error("Cannot find available content!")
            logger.debug(e)
        chat = prismarinechat(content)
        # logger.debug(chat)
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
                for player in players:
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
        chatjson = json.loads(e["formattedMessage"])
        chat = prismarinechat(chatjson)
        for msg in color_converter.convert_minecraft_to_miniworld(chat.toMotd()).split(
            "\n"
        ):
            self.miniplayer.send_msg(msg)
        logger.debug(f"[Chat] {chat.toAnsi()}")

    def on_packet(self, jsondata: dict, metadata: dict, buffer=None, fullbuffer=None):
        # logger.debug(f"mcpacket: {metadata}\n{jsondata}")
        on_event(metadata["name"], self, jsondata, metadata)

    def end(self):
        self.client.end()

    def remove(self):
        self.chunkmgr.running = False
        self.end()

    def chat(self, content: str):
        self.client.chat(content)

    def send(self, name: str, message: dict):
        self.client.write(name, message)

    def get_chunks(self):
        if self.chunkmgr.cacheParsedChunks.length > 0:
            compressed_chunks = self.chunkmgr.compressedChunks.blobValueOf()
            chunks = ormsgpack.unpackb(zlib.decompress(compressed_chunks))
            self.on_packet(chunks, {"name": "parsed_chunk"})

    def get_chunks_task(self):
        while self.running:
            time.sleep(0.2)
            self.get_chunks()

    def load_events(self):
        for event in events:
            if event not in self.on_events:
                self.client.on(event, self.on_packet)
                self.on_events.append(event)

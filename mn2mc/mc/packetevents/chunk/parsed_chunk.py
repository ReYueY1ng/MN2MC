from __future__ import annotations

import queue

from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents.chunk.chunk_parser import (
    create_worker_threads,
    send_air_chunk,
    send_block_updates,
)

chunkqueue = queue.Queue()


def on_recv(client: MCClient, chunklist: list, metadata: dict) -> None:
    for chunkdata in chunklist:
        chunkqueue.put((client, chunkdata))


def parse_done(client: MCClient, chunkdata: dict):
    cx = -chunkdata["x"] - 1
    cz = chunkdata["z"]
    send_air_chunk(client.miniplayer, cx, cz)
    send_block_updates(client.miniplayer, cx, cz, chunkdata["blocks"], flush_threshold=6000)


def stop():
    chunkqueue.shutdown()


def _process(data):
    parse_done(data[0], data[1])


create_worker_threads(_process, chunkqueue)

add_event("parsed_chunk", on_recv)

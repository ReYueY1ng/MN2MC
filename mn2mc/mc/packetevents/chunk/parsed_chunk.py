from __future__ import annotations

import queue

import mn2mc.config as config
from mn2mc.mc.client import MCClient
from mn2mc.mc.packet import add_event
from mn2mc.mc.packetevents.chunk.chunk_parser import (
    create_worker_threads,
    send_air_chunk,
    send_block_updates,
    send_fast_chunk,
)

chunkqueue = queue.Queue()


def on_recv(client: MCClient, chunklist: list, metadata: dict) -> None:
    for chunkdata in chunklist:
        chunkqueue.put((client, chunkdata))


def parse_done(client: MCClient, chunkdata: dict):
    cx = -chunkdata["x"] - 1
    cz = chunkdata["z"]
    if config.mc.fast_chunk_conversion:
        send_fast_chunk(client.miniplayer, cx, cz, chunkdata["blocks"], chunkdata.get("lights"))
    else:
        send_air_chunk(client.miniplayer, cx, cz)
        send_block_updates(client.miniplayer, cx, cz, chunkdata["blocks"], flush_threshold=4096)


def stop():
    try:
        chunkqueue.shutdown()
    except queue.ShutDown:
        pass


def _process(data):
    parse_done(data[0], data[1])


create_worker_threads(_process, chunkqueue)

add_event("parsed_chunk", on_recv)

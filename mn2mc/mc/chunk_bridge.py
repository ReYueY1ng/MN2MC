"""Chunk data bridge between MC and Mini World."""

from __future__ import annotations

import threading
import time
import zlib
from typing import TYPE_CHECKING

import javascript
import ormsgpack
from javascript.events import TaskState
from loguru import logger

import mn2mc.config as config
from mn2mc.mc.chunk_transport import (
    ChunkTransport,
    KRENTransport,
    TCPTransport,
    detect_transport,
)
from mn2mc.mc.packet import on_event

if TYPE_CHECKING:
    from mn2mc.mc.client import MCClient

ChunkManager = javascript.require("./chunk.js")


class MCChunkBridge:
    _mc_client: MCClient
    _running_event: threading.Event
    """Manages chunk data parsing and forwarding."""

    def __init__(self, mc_client, mcprotocol_client, registry) -> None:
        version = config.mc.version
        self._mc_client = mc_client

        mode = detect_transport(config.mc.chunk_transport)
        channel_name = f"mn2mc_chunk_{id(self)}"
        buffer_size = config.mc.kren_buffer_size

        if mode == "kren":
            try:
                self.chunkmgr = ChunkManager(
                    version, mc_client, mcprotocol_client, registry,
                    "kren", channel_name, buffer_size,
                )
                self._transport: ChunkTransport = KRENTransport(channel_name)
                logger.info("Chunk transport: kren")
            except Exception as e:
                logger.warning(
                    f"KREN transport failed ({e}), falling back to TCP"
                )
                mode = "tcp"

        if mode == "tcp":
            self.chunkmgr = ChunkManager(
                version, mc_client, mcprotocol_client, registry,
                "tcp", channel_name, buffer_size,
            )
            port = None
            for _ in range(50):
                try:
                    port = self.chunkmgr.transportPort
                except Exception:
                    pass
                if port is not None:
                    break
                time.sleep(0.1)
            if port is None:
                raise RuntimeError("ChunkManager TCP transport port not available after 5s")
            self._transport = TCPTransport("127.0.0.1", port)
            logger.info("Chunk transport: tcp")

        self._writer_closed = False
        self._stopped = False
        self.get_chunk_thread: threading.Thread | None = None

    def start(self, miniplayer_name: str, running_event: threading.Event) -> None:
        """Start the chunk polling thread."""
        self._running_event = running_event

        @javascript.AsyncTask(start=True)
        def _poll_chunks(task: TaskState) -> None:
            """Poll for new chunk data on a background thread."""
            while self._running_event.is_set() and not self._writer_closed:
                time.sleep(0.01)
                self._get_chunks(self._running_event)


    def _get_chunks(self, running_event: threading.Event) -> None:
        """Fetch and forward parsed chunks if available."""
        if not running_event.is_set():
            return
        try:
            data = self._transport.recv()
        except (ConnectionError, OSError) as e:
            logger.warning(f"Chunk transport connection lost: {e}")
            self._writer_closed = True
            return
        if data is None:
            # KREN: check if writer closed
            if isinstance(self._transport, KRENTransport) and self._transport.writer_closed:
                logger.warning("KREN writer closed, stopping chunk polling")
                self._writer_closed = True
            return
        try:
            chunks = ormsgpack.unpackb(zlib.decompress(data))
        except (zlib.error, Exception) as e:
            logger.warning(f"Failed to decode chunk transport data: {e}")
            return
        on_event("parsed_chunk", self._mc_client, chunks, {"name": "parsed_chunk"})

    def stop(self) -> None:
        """Stop the chunk manager (idempotent)."""
        if self._stopped:
            return
        self._stopped = True
        self._writer_closed = True
        if hasattr(self, "_transport"):
            self._transport.close()
        if hasattr(self, "chunkmgr"):
            self.chunkmgr.running = False

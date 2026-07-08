"""Chunk data bridge between MC and Mini World."""

from __future__ import annotations
from loguru import logger
from javascript.events import TaskState

import threading
import time
import zlib
from typing import TYPE_CHECKING

import javascript
import ormsgpack

import mn2mc.config as config
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
        self.chunkmgr = ChunkManager(version, mc_client, mcprotocol_client, registry)
        self.get_chunk_thread: threading.Thread | None = None

    def start(self, miniplayer_name: str, running_event: threading.Event) -> None:
        """Start the chunk polling thread."""

        """
        self.get_chunk_thread = threading.Thread(
            target=self._poll_chunks,
            name=f"({miniplayer_name}) Get chunk thread",
            daemon=True,
            args=(running_event,),
        )
        self.get_chunk_thread.start()
        """
        self._running_event = running_event

        @javascript.AsyncTask(start=True)
        def _poll_chunks(task: TaskState) -> None:
            """Poll for new chunk data on a background thread."""
            while self._running_event.is_set():
                time.sleep(0.2)
                self._get_chunks(self._running_event)


    def _get_chunks(self, running_event: threading.Event) -> None:
        """Fetch and forward parsed chunks if available."""
        if running_event.is_set() and self.chunkmgr.cacheParsedChunks.length > 0:
            compressed_chunks = self.chunkmgr.compressedChunks.blobValueOf()
            chunks = ormsgpack.unpackb(zlib.decompress(compressed_chunks))
            on_event("parsed_chunk", self._mc_client, chunks, {"name": "parsed_chunk"})

    def stop(self) -> None:
        """Stop the chunk manager."""
        if hasattr(self, "chunkmgr"):
            self.chunkmgr.running = False

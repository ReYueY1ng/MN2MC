"""Chunk data transport abstractions for receiving parsed chunk data from JS.

Provides two transport mechanisms:
- KRENTransport: shared-memory via kren library (Linux uses /dev/shm, Windows uses pipe, macOS not supported)
- TCPTransport: TCP socket with length-prefixed frames (universal fallback)

Python side is always the Reader/Client; JS side is the Writer/Server.
"""

from __future__ import annotations

import os
import socket
import struct
import time
from abc import ABC, abstractmethod

from loguru import logger


class ChunkTransport(ABC):
    """Abstract base class for chunk data transports."""

    @abstractmethod
    def recv(self) -> bytes | None:
        """Receive one chunk data frame. Returns bytes or None if no data available."""

    @abstractmethod
    def close(self) -> None:
        """Release transport resources."""

    @staticmethod
    @abstractmethod
    def is_available() -> bool:
        """Check if this transport is available on the current platform."""


def detect_transport(config_chunk_transport: str) -> str:
    """Detect which transport to use based on config value.

    Args:
        config_chunk_transport: "auto", "kren", or "tcp".

    Returns:
        "kren" or "tcp".
    """
    if config_chunk_transport in ("kren", "tcp"):
        return config_chunk_transport

    try:
        import kren
        test_name = f"_kren_probe_{os.getpid()}"
        writer = kren.Writer(test_name, 64)
        writer.write(b"test")
        reader = kren.Reader(test_name)
        data = reader.try_read()
        del reader, writer
        if data == b"test":
            logger.info("kren available, using KREN transport")
            return "kren"
        logger.info("kren probe failed (read mismatch), falling back to TCP")
        return "tcp"
    except ModuleNotFoundError:
        logger.info("kren module not found, falling back to TCP transport")
        return "tcp"
    except (OSError, Exception) as e:
        logger.info(f"kren probe failed ({e}), falling back to TCP transport")
        return "tcp"


class KRENTransport(ChunkTransport):
    """Shared-memory transport via kren library. Python is Reader; JS is Writer."""

    def __init__(self, channel_name: str) -> None:
        import kren

        self._reader = kren.Reader(channel_name)
        logger.debug(f"KRENTransport: opened reader on channel '{channel_name}'")

    def recv(self) -> bytes | None:
        """Non-blocking read from shared memory channel."""
        return self._reader.try_read()

    @property
    def writer_closed(self) -> bool:
        """True if the reader has been released (writer closed)."""
        return self._reader is None

    def close(self) -> None:
        """Release the kren reader."""
        self._reader = None

    @staticmethod
    def is_available() -> bool:
        try:
            import kren
            test_name = f"_kren_avail_{os.getpid()}"
            w = kren.Writer(test_name, 64)
            del w
            return True
        except Exception:
            return False


class TCPTransport(ChunkTransport):
    """TCP socket transport with length-prefixed frames. Python is client; JS is server.

    Frame protocol: [4-byte big-endian length][compressed data]
    """

    def __init__(self, host: str, port: int) -> None:
        self._sock: socket.socket | None = None
        self._buffer = b""
        self._connect_with_retry(host, port)

    def _connect_with_retry(self, host: str, port: int) -> None:
        """Connect to TCP server with retry (3 attempts, 100ms delay)."""
        for attempt in range(3):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.01)
                sock.connect((host, port))
                self._sock = sock
                logger.debug(f"TCPTransport: connected to {host}:{port}")
                return
            except (ConnectionError, OSError) as e:
                logger.warning(
                    f"TCPTransport: connection attempt {attempt + 1}/3 failed: {e}"
                )
                if attempt < 2:
                    time.sleep(0.1)
        raise ConnectionError(
            f"TCPTransport: failed to connect to {host}:{port} after 3 attempts"
        )

    def recv(self) -> bytes | None:
        """Read one length-prefixed frame from the socket. Non-blocking."""
        if self._sock is None:
            return None

        try:
            data = self._sock.recv(65536)
            if not data:
                return None
            self._buffer += data
        except (TimeoutError, BlockingIOError, OSError):
            # No data available (non-blocking)
            pass

        # Try to parse a complete frame: [4-byte BE length][data]
        if len(self._buffer) < 4:
            return None

        frame_len = struct.unpack(">I", self._buffer[:4])[0]
        total = 4 + frame_len
        if len(self._buffer) < total:
            return None

        frame_data = self._buffer[4:total]
        self._buffer = self._buffer[total:]
        return frame_data

    def close(self) -> None:
        """Close the TCP socket."""
        if self._sock is not None:
            try:
                self._sock.close()
            except OSError:
                pass
            self._sock = None

    @staticmethod
    def is_available() -> bool:
        """TCP is always available."""
        return True

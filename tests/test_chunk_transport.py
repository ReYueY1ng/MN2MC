"""Integration tests for chunk transport — detect_transport, TCPTransport, KRENTransport.

Run standalone: python tests/test_chunk_transport.py
Run via pytest:  pytest tests/test_chunk_transport.py -v
"""

from __future__ import annotations

import os
import socket
import struct
import subprocess
import sys
import time
import unittest

# Ensure project root is on sys.path for standalone execution
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)


# ---------------------------------------------------------------------------
# Test 1-3: detect_transport
# ---------------------------------------------------------------------------

class TestDetectTransport(unittest.TestCase):
    """Test detect_transport() with different config values."""

    def test_auto_returns_kren_or_tcp(self):
        """detect_transport("auto") must return "kren" or "tcp"."""
        from mn2mc.mc.chunk_transport import detect_transport

        result = detect_transport("auto")
        self.assertIn(result, ("kren", "tcp"))

    def test_tcp_always_returns_tcp(self):
        """detect_transport("tcp") must always return "tcp"."""
        from mn2mc.mc.chunk_transport import detect_transport

        self.assertEqual(detect_transport("tcp"), "tcp")

    def test_kren_returns_kren_or_raises(self):
        """detect_transport("kren") returns "kren" directly (no availability check)."""
        from mn2mc.mc.chunk_transport import detect_transport

        self.assertEqual(detect_transport("kren"), "kren")


# ---------------------------------------------------------------------------
# Test 4: TCPTransport — end-to-end framed data exchange
# ---------------------------------------------------------------------------

def _tcp_server_script(port: int, data: bytes) -> str:
    """Return a Python one-liner that serves one framed message then exits."""
    hex_data = data.hex()
    return (
        "import socket, struct, sys; "
        f"s=socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); "
        f"s.bind(('127.0.0.1',{port})); s.listen(1); "
        "c,_=s.accept(); "
        f"c.sendall(struct.pack('>I',{len(data)})+bytes.fromhex('{hex_data}')); "
        "c.close(); s.close()"
    )


def _find_free_port() -> int:
    """Find a free TCP port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


class TestTCPTransport(unittest.TestCase):
    """Test TCPTransport: connect, send/receive framed data."""

    def test_recv_single_frame(self):
        """TCPTransport receives a single length-prefixed frame correctly."""
        from mn2mc.mc.chunk_transport import TCPTransport

        payload = b"hello chunk data"
        port = _find_free_port()

        server = subprocess.Popen(
            [sys.executable, "-c", _tcp_server_script(port, payload)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Give the server time to bind
        time.sleep(0.3)

        transport = None
        try:
            transport = TCPTransport("127.0.0.1", port)
            # recv may need a couple of calls due to non-blocking reads
            result = None
            for _ in range(50):
                result = transport.recv()
                if result is not None:
                    break
                time.sleep(0.05)

            self.assertIsNotNone(result, "TCPTransport.recv() returned None — no frame received")
            self.assertEqual(result, payload)
        finally:
            if transport is not None:
                transport.close()
            server.wait(timeout=5)

    def test_recv_multiple_frames(self):
        """TCPTransport handles multiple frames arriving in one TCP stream."""
        from mn2mc.mc.chunk_transport import TCPTransport

        frames = [b"frame_one", b"frame_two", b"frame_three"]
        port = _find_free_port()

        parts = []
        for f in frames:
            parts.append(f"struct.pack('>I',{len(f)})+{f!r}")
        payload_expr = "+".join(parts)

        script = (
            "import socket, struct, time; "
            f"s=socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); "
            f"s.bind(('127.0.0.1',{port})); s.listen(1); "
            "c,_=s.accept(); "
            f"c.sendall({payload_expr}); "
            "time.sleep(1); c.close(); s.close()"
        )

        server = subprocess.Popen(
            [sys.executable, "-c", script],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(0.3)

        transport = None
        try:
            transport = TCPTransport("127.0.0.1", port)
            received = []
            for _ in range(100):
                chunk = transport.recv()
                if chunk is not None:
                    received.append(chunk)
                    if len(received) == len(frames):
                        break
                time.sleep(0.05)

            self.assertEqual(len(received), len(frames), f"Expected {len(frames)} frames, got {len(received)}")
            for expected, actual in zip(frames, received):
                self.assertEqual(expected, actual)
        finally:
            if transport is not None:
                transport.close()
            server.wait(timeout=5)

    def test_recv_empty_payload(self):
        """TCPTransport handles a zero-length frame payload."""
        from mn2mc.mc.chunk_transport import TCPTransport

        payload = b""
        port = _find_free_port()

        server = subprocess.Popen(
            [sys.executable, "-c", _tcp_server_script(port, payload)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(0.3)

        transport = None
        try:
            transport = TCPTransport("127.0.0.1", port)
            result = None
            for _ in range(50):
                result = transport.recv()
                if result is not None:
                    break
                time.sleep(0.05)

            self.assertIsNotNone(result, "TCPTransport.recv() returned None for empty payload")
            self.assertEqual(result, b"")
        finally:
            if transport is not None:
                transport.close()
            server.wait(timeout=5)

    def test_connection_retry(self):
        """TCPTransport raises ConnectionError when server is unreachable."""
        from mn2mc.mc.chunk_transport import TCPTransport

        # Use a port that's unlikely to have a server
        with self.assertRaises(ConnectionError):
            TCPTransport("127.0.0.1", 1)

    def test_close_idempotent(self):
        """TCPTransport.close() can be called multiple times without error."""
        from mn2mc.mc.chunk_transport import TCPTransport

        port = _find_free_port()
        payload = b"close_test"

        server = subprocess.Popen(
            [sys.executable, "-c", _tcp_server_script(port, payload)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        time.sleep(0.3)

        try:
            transport = TCPTransport("127.0.0.1", port)
            # Drain one frame so the socket is active
            for _ in range(50):
                if transport.recv() is not None:
                    break
                time.sleep(0.05)

            transport.close()
            transport.close()  # second close should not raise
        finally:
            server.wait(timeout=5)


# ---------------------------------------------------------------------------
# Test 5: KRENTransport — shared-memory transport (skip if kren unavailable)
# ---------------------------------------------------------------------------

class TestKRENTransport(unittest.TestCase):
    """Test KRENTransport if kren is available."""

    @staticmethod
    def _kren_available() -> bool:
        try:
            import kren  # noqa: F401
            return os.path.exists("/dev/shm")
        except ModuleNotFoundError:
            return False

    def test_kren_writer_reader_roundtrip(self):
        """KRENTransport Reader can read data written by kren Writer."""
        if not self._kren_available():
            self.skipTest("kren not available")

        import kren

        from mn2mc.mc.chunk_transport import KRENTransport

        channel = f"test_chunk_transport_{os.getpid()}"
        payload = b"kren shared memory test data"

        # Write data via kren Writer, then read via KRENTransport
        writer = kren.Writer(channel, 1024 * 1024)
        transport = KRENTransport(channel)

        try:
            writer.write(payload)

            result = None
            for _ in range(50):
                result = transport.recv()
                if result is not None:
                    break
                time.sleep(0.01)

            self.assertIsNotNone(result, "KRENTransport.recv() returned None — no data received")
            self.assertEqual(result, payload)
        finally:
            transport.close()
            del writer  # release kren writer

    def test_kren_recv_empty_returns_none(self):
        """KRENTransport.recv() returns None when no data is available."""
        if not self._kren_available():
            self.skipTest("kren not available")

        import kren

        from mn2mc.mc.chunk_transport import KRENTransport

        channel = f"test_chunk_empty_{os.getpid()}"

        writer = kren.Writer(channel, 1024 * 1024)
        transport = KRENTransport(channel)

        try:
            result = transport.recv()
            self.assertIsNone(result, "KRENTransport.recv() should return None when channel is empty")
        finally:
            transport.close()
            del writer

    def test_kren_is_available(self):
        """KRENTransport.is_available() matches actual kren availability."""
        from mn2mc.mc.chunk_transport import KRENTransport

        expected = self._kren_available()
        self.assertEqual(KRENTransport.is_available(), expected)


# ---------------------------------------------------------------------------
# Test: ChunkTransport ABC interface
# ---------------------------------------------------------------------------

class TestChunkTransportABC(unittest.TestCase):
    """Verify ChunkTransport cannot be instantiated directly."""

    def test_cannot_instantiate_abc(self):
        """ChunkTransport is abstract and cannot be instantiated."""
        from mn2mc.mc.chunk_transport import ChunkTransport

        with self.assertRaises(TypeError):
            ChunkTransport()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    unittest.main()

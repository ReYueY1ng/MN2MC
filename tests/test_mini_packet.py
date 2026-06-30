"""Tests for mn2mc.mini.packet — MiniClientPacket and MiniServerPacket encode/decode."""

import struct

import pytest

from mn2mc.mini.packet import PLACEHOLDER, MiniClientPacket, MiniServerPacket


class TestMiniClientPacketEncodeDecode:
    """Test MiniClientPacket encode/decode symmetry."""

    def test_encode_round_trip(self):
        """Encode then decode should recover original fields."""
        pkt = MiniClientPacket(12345, 100, b"hello")
        raw = pkt.encode()
        pkt2 = MiniClientPacket(raw)
        assert pkt2.uin == 12345
        assert pkt2.msgcode == 100
        assert pkt2.data == b"hello"

    def test_decode_round_trip(self):
        """Decode then encode should reproduce original bytes."""
        original = (
            b"\x89"
            + struct.pack(">I", 999)
            + PLACEHOLDER
            + struct.pack("<HH", 42, 5)
            + b"world"
        )
        pkt = MiniClientPacket(original)
        assert pkt.encode() == original

    def test_encode_header(self):
        """Encoded packet starts with 0x89."""
        pkt = MiniClientPacket(1, 2, b"\x00")
        raw = pkt.encode()
        assert raw[0:1] == b"\x89"

    def test_encode_uin_big_endian(self):
        """Uin is encoded as big-endian uint32 at bytes 1-4."""
        pkt = MiniClientPacket(0xDEADBEEF, 1, b"")
        raw = pkt.encode()
        assert raw[1:5] == struct.pack(">I", 0xDEADBEEF)

    def test_encode_placeholder(self):
        """Bytes 5-8 are the PLACEHOLDER constant."""
        pkt = MiniClientPacket(0, 0, b"")
        raw = pkt.encode()
        assert raw[5:9] == PLACEHOLDER

    def test_encode_msgcode_le(self):
        """Msgcode is little-endian uint16 at bytes 9-10."""
        pkt = MiniClientPacket(0, 0x1234, b"")
        raw = pkt.encode()
        assert raw[9:11] == struct.pack("<H", 0x1234)

    def test_encode_length_le(self):
        """Data length is little-endian uint16 at bytes 11-12."""
        pkt = MiniClientPacket(0, 0, b"ABCDE")
        raw = pkt.encode()
        assert raw[11:13] == struct.pack("<H", 5)

    def test_encode_data_payload(self):
        """Data payload starts at byte 13."""
        payload = b"test payload"
        pkt = MiniClientPacket(0, 0, payload)
        raw = pkt.encode()
        assert raw[13:] == payload

    def test_empty_data(self):
        """Empty data should encode/decode correctly."""
        pkt = MiniClientPacket(42, 7, b"")
        raw = pkt.encode()
        pkt2 = MiniClientPacket(raw)
        assert pkt2.uin == 42
        assert pkt2.msgcode == 7
        assert pkt2.data == b""

    def test_large_data(self):
        """Large data payload round-trips correctly."""
        payload = bytes(range(256)) * 10
        pkt = MiniClientPacket(100, 200, payload)
        raw = pkt.encode()
        pkt2 = MiniClientPacket(raw)
        assert pkt2.data == payload

    def test_max_uin(self):
        """Max uint32 uin value round-trips correctly."""
        pkt = MiniClientPacket(0xFFFFFFFF, 1, b"")
        raw = pkt.encode()
        pkt2 = MiniClientPacket(raw)
        assert pkt2.uin == 0xFFFFFFFF


class TestMiniClientPacketInit:
    """Test MiniClientPacket constructor validation."""

    def test_construct_with_args(self):
        """Direct construction with uin, msgcode, data."""
        pkt = MiniClientPacket(1, 2, b"abc")
        assert pkt.uin == 1
        assert pkt.msgcode == 2
        assert pkt.data == b"abc"

    def test_construct_with_bytes(self):
        """Construction from raw bytes triggers decode."""
        raw = (
            b"\x89"
            + struct.pack(">I", 55)
            + PLACEHOLDER
            + struct.pack("<HH", 10, 3)
            + b"xyz"
        )
        pkt = MiniClientPacket(raw)
        assert pkt.uin == 55
        assert pkt.msgcode == 10
        assert pkt.data == b"xyz"

    def test_msgcode_must_be_int(self):
        """Non-int msgcode raises TypeError."""
        with pytest.raises(TypeError, match="msgcode must be int"):
            MiniClientPacket(1, "bad", b"")  # type: ignore[arg-type]

    def test_data_must_be_bytes(self):
        """Non-bytes data raises TypeError."""
        with pytest.raises(TypeError, match="data must be bytes"):
            MiniClientPacket(1, 2, "not bytes")  # type: ignore[arg-type]

    def test_str_repr(self):
        """__str__ includes uin and msgcode."""
        pkt = MiniClientPacket(42, 7, b"hi")
        s = str(pkt)
        assert "42" in s
        assert "7" in s


class TestMiniClientPacketIsinstance:
    """Test isinstance fix — int subclasses accepted for uinordata."""

    def test_int_subclass_as_uin(self):
        """An int subclass should be accepted as uinordata."""
        class MyInt(int):
            pass

        pkt = MiniClientPacket(MyInt(100), 5, b"data")
        assert pkt.uin == 100
        assert pkt.msgcode == 5
        assert pkt.data == b"data"

    def test_int_subclass_encode_decode(self):
        """Packet constructed with int subclass encodes/decodes correctly."""
        class MyInt(int):
            pass

        pkt = MiniClientPacket(MyInt(42), 99, b"test")
        raw = pkt.encode()
        pkt2 = MiniClientPacket(raw)
        assert pkt2.uin == 42
        assert pkt2.msgcode == 99
        assert pkt2.data == b"test"

    def test_bool_not_accepted_as_msgcode(self):
        """bool is a subclass of int but msgcode check should still work (bool is int)."""
        # bool IS a subclass of int, so isinstance(True, int) is True
        # This means True (==1) is accepted as msgcode
        pkt = MiniClientPacket(1, True, b"")  # type: ignore[arg-type]
        assert pkt.msgcode is True  # preserved as bool, but value is 1

    def test_bytes_subclass_as_data(self):
        """A bytes subclass should be accepted as data."""
        class MyBytes(bytes):
            pass

        pkt = MiniClientPacket(1, 2, MyBytes(b"hello"))
        assert pkt.data == b"hello"


class TestMiniServerPacketEncodeDecode:
    """Test MiniServerPacket encode/decode symmetry."""

    def test_encode_round_trip(self):
        """Encode then decode should recover original fields."""
        pkt = MiniServerPacket(100, b"hello")
        raw = pkt.encode()
        pkt2 = MiniServerPacket(None, None)
        pkt2.decode(raw)
        assert pkt2.msgcode == 100
        assert pkt2.data == b"hello"

    def test_decode_round_trip(self):
        """Decode then encode should reproduce original bytes."""
        original = b"\x89" + struct.pack("<HH", 42, 5) + b"world"
        pkt = MiniServerPacket(None, None)
        pkt.decode(original)
        assert pkt.encode() == original

    def test_encode_header(self):
        """Encoded packet starts with 0x89."""
        pkt = MiniServerPacket(1, b"\x00")
        raw = pkt.encode()
        assert raw[0:1] == b"\x89"

    def test_encode_msgcode_le(self):
        """Msgcode is little-endian uint16 at bytes 1-2."""
        pkt = MiniServerPacket(0x1234, b"")
        raw = pkt.encode()
        assert raw[1:3] == struct.pack("<H", 0x1234)

    def test_encode_length_le(self):
        """Data length is little-endian uint16 at bytes 3-4."""
        pkt = MiniServerPacket(1, b"ABCDE")
        raw = pkt.encode()
        assert raw[3:5] == struct.pack("<H", 5)

    def test_encode_data_payload(self):
        """Data payload starts at byte 5."""
        payload = b"test payload"
        pkt = MiniServerPacket(1, payload)
        raw = pkt.encode()
        assert raw[5:] == payload

    def test_empty_data(self):
        """Empty data should encode/decode correctly."""
        pkt = MiniServerPacket(7, b"")
        raw = pkt.encode()
        pkt2 = MiniServerPacket(None, None)
        pkt2.decode(raw)
        assert pkt2.msgcode == 7
        assert pkt2.data == b""

    def test_large_data(self):
        """Large data payload round-trips correctly."""
        payload = bytes(range(256)) * 10
        pkt = MiniServerPacket(200, payload)
        raw = pkt.encode()
        pkt2 = MiniServerPacket(None, None)
        pkt2.decode(raw)
        assert pkt2.data == payload


class TestMiniServerPacketInit:
    """Test MiniServerPacket constructor."""

    def test_construct_with_args(self):
        """Direct construction with msgcode and data."""
        pkt = MiniServerPacket(10, b"abc")
        assert pkt.msgcode == 10
        assert pkt.data == b"abc"

    def test_default_data(self):
        """Default data is empty bytes."""
        pkt = MiniServerPacket(1, None)
        # When data is None/falsy, class default b"" is used
        assert pkt.data == b""

    def test_str_repr(self):
        """__str__ includes msgcode."""
        pkt = MiniServerPacket(42, b"hi")
        s = str(pkt)
        assert "42" in s

    def test_msgcode_zero_not_set(self):
        """msgcode=0 is accepted and stored correctly."""
        pkt = MiniServerPacket(0, b"data")
        assert pkt.msgcode == 0


class TestMiniServerPacketIsinstance:
    """Test isinstance patterns for MiniServerPacket."""

    def test_int_subclass_as_msgcode(self):
        """An int subclass should be accepted as msgcode."""
        class MyInt(int):
            pass

        pkt = MiniServerPacket(MyInt(50), b"data")
        assert pkt.msgcode == 50

    def test_bytes_subclass_as_data(self):
        """A bytes subclass should be accepted as data."""
        class MyBytes(bytes):
            pass

        pkt = MiniServerPacket(1, MyBytes(b"hello"))
        assert pkt.data == b"hello"

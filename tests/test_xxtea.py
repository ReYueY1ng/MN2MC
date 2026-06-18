"""Tests for mn2mc.utils.xxtea — XXTEA encryption, compression, and packing utilities."""

import pytest
from mn2mc.utils import xxtea


class TestPackUnpack:
    """Test pack/unpack round-trip symmetry."""

    def test_pack_returns_bytes(self):
        result = xxtea.pack(b"hello")
        assert isinstance(result, bytes)

    def test_unpack_returns_bytes(self):
        packed = xxtea.pack(b"hello")
        result = xxtea.unpack(packed)
        assert isinstance(result, bytes)

    def test_roundtrip_short_data(self):
        data = b"hello"
        assert xxtea.unpack(xxtea.pack(data)) == data

    def test_roundtrip_empty_data(self):
        data = b""
        assert xxtea.unpack(xxtea.pack(data)) == data

    def test_roundtrip_binary_data(self):
        data = bytes(range(256))
        assert xxtea.unpack(xxtea.pack(data)) == data

    def test_roundtrip_random_lengths(self):
        """Various lengths including non-aligned-to-4."""
        for n in [1, 3, 4, 7, 16, 100, 1024]:
            data = b"\xab" * n
            assert xxtea.unpack(xxtea.pack(data)) == data

    def test_pack_pads_to_4_byte_boundary(self):
        """packed length (excluding 4-byte header) must be 4-byte aligned."""
        for n in [1, 2, 3, 4, 5]:
            packed = xxtea.pack(b"\x00" * n)
            # total length = 4 (header) + data + padding
            assert (len(packed) - 4) % 4 == 0


class TestEncryptDecrypt:
    """Test encrypt/decrypt round-trip symmetry."""

    def test_roundtrip_short_string(self):
        data = b"hello world"
        assert xxtea.decrypt(xxtea.encrypt(data)) == data

    def test_encrypt_empty_raises(self):
        """XXTEA requires >= 8 bytes; empty data after pack is only 4 bytes."""
        with pytest.raises(ValueError, match="Data length"):
            xxtea.encrypt(b"")

    def test_roundtrip_binary(self):
        data = bytes(range(256))
        assert xxtea.decrypt(xxtea.encrypt(data)) == data

    def test_roundtrip_long_data(self):
        data = b"A" * 4096
        assert xxtea.decrypt(xxtea.encrypt(data)) == data

    def test_encrypt_returns_bytes(self):
        result = xxtea.encrypt(b"test")
        assert isinstance(result, bytes)

    def test_encrypt_changes_data(self):
        """Encrypted output should differ from input."""
        data = b"hello"
        assert xxtea.encrypt(data) != data

    def test_different_inputs_differ(self):
        """Different plaintexts should produce different ciphertexts."""
        a = xxtea.encrypt(b"hello")
        b = xxtea.encrypt(b"world")
        assert a != b


class TestEncryptZipDecryptUnzip:
    """Test encrypt_zip/decrypt_unzip round-trip symmetry."""

    def test_roundtrip_bytes(self):
        data = b"hello world, this is some data for compression"
        assert xxtea.decrypt_unzip(xxtea.encrypt_zip(data)) == data

    def test_roundtrip_empty_bytes(self):
        data = b""
        assert xxtea.decrypt_unzip(xxtea.encrypt_zip(data)) == data

    def test_roundtrip_large_bytes(self):
        data = b"repeat " * 1000
        assert xxtea.decrypt_unzip(xxtea.encrypt_zip(data)) == data

    def test_roundtrip_binary(self):
        data = bytes(range(256))
        assert xxtea.decrypt_unzip(xxtea.encrypt_zip(data)) == data

    def test_encrypt_zip_returns_bytes(self):
        result = xxtea.encrypt_zip(b"test")
        assert isinstance(result, bytes)

    def test_encrypt_zip_string_input_returns_bytes(self):
        """Regression: encrypt_zip('str') must return bytes, not crash.

        Previously the check was `if data is str:` (identity, always False),
        fixed to `if isinstance(data, str):`.
        """
        result = xxtea.encrypt_zip("hello string")
        assert isinstance(result, bytes)

    def test_roundtrip_string_input(self):
        """encrypt_zip('string') should decrypt back to the encoded bytes."""
        text = "hello string"
        result = xxtea.decrypt_unzip(xxtea.encrypt_zip(text))
        assert result == text.encode()

    def test_string_and_bytes_produce_same_result(self):
        """encrypt_zip('x') == encrypt_zip(b'x') after the isinstance fix."""
        assert xxtea.encrypt_zip("test data") == xxtea.encrypt_zip(b"test data")

    def test_compresses_data(self):
        """Compressed+encrypted should be smaller than raw for compressible data."""
        data = b"aaaa" * 1000
        compressed = xxtea.encrypt_zip(data)
        plain = xxtea.encrypt(data)
        assert len(compressed) < len(plain)

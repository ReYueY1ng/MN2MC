import struct
import zlib

import xxtea

xxtea_key = bytes.fromhex("b48e6ef44ed13eee606141750e729cf4")

def pack(data):
    """Pack data with a 4-byte big-endian length prefix, padded to a 4-byte boundary."""
    packdata = struct.pack(f'>I{len(data)}s', len(data), data)
    if len(packdata) % 4 != 0:
        packdata += b'\x00' * (4 - len(packdata) % 4)
    return packdata

def unpack(data):
    """Unpack data by reading the 4-byte big-endian length prefix."""
    length = struct.unpack('>I', data[:4])[0]
    return data[4:length+4]

def encrypt(data):
    """Encrypt data using XXTEA with the shared key."""
    return xxtea.encrypt(pack(data), xxtea_key, False)

def encrypt_zip(data):
    """Compress data with zlib, then encrypt using XXTEA."""
    if isinstance(data, str):
        data = data.encode()
    return xxtea.encrypt(pack(zlib.compress(data)), xxtea_key, False)

def decrypt(data):
    """Decrypt XXTEA-encrypted data and unpack the length prefix."""
    return unpack(xxtea.decrypt(data, xxtea_key, False))

def decrypt_unzip(data):
    """Decrypt XXTEA-encrypted data, unpack, and decompress with zlib."""
    return zlib.decompress(unpack(xxtea.decrypt(data, xxtea_key, False)))

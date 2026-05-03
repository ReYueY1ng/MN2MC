import struct
import zlib

import xxtea

xxtea_key = b''

def pack(data):
    packdata = struct.pack(f'>I{len(data)}s', len(data), data)
    if len(packdata) % 4 != 0:
        packdata += b'\x00' * (4 - len(packdata) % 4)
    return packdata

def unpack(data):
    length = struct.unpack('>I', data[:4])[0]
    return data[4:length+4]

def encrypt(data):
    return xxtea.encrypt(pack(data), xxtea_key, False)

def encrypt_zip(data):
    if data is str:
        data = data.encode()
    return xxtea.encrypt(pack(zlib.compress(data)), xxtea_key, False)

def decrypt(data):
    return unpack(xxtea.decrypt(data, xxtea_key, False))

def decrypt_unzip(data):
    return zlib.decompress(unpack(xxtea.decrypt(data, xxtea_key, False)))
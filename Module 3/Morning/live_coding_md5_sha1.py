"""
Write a Python program which computes the SHA-1 and MD5 hashes of a given bytearray 
Test with various fixed bytearrays: b’Yellow Submarine’ for example

Use Cryptography library in Python

Test for the avalanche effect
Small change in input gives large change in output
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

inputText = b'Yellow Submarine'

# Compute MD5 hash of input text
md5hash = hashes.Hash(hashes.MD5(), default_backend())
md5hash.update(inputText)
md5digest = md5hash.finalize()
print(md5digest.hex())

# Compute SHA-1 hash of input text
sha1hash = hashes.Hash(hashes.SHA1(), default_backend())
sha1hash.update(inputText)
sha1digest = sha1hash.finalize()
print(sha1digest.hex())

# A slightly different input text
inputText2 = b'Yellow submarine'
print("Changing capitol S to small s")
# Compute MD5 hash of input text
md5hash = hashes.Hash(hashes.MD5(), default_backend())
md5hash.update(inputText2)
md5digest = md5hash.finalize()
print(md5digest.hex())

# Compute SHA-1 hash of input text
sha1hash = hashes.Hash(hashes.SHA1(), default_backend())
sha1hash.update(inputText2)
sha1digest = sha1hash.finalize()
print(sha1digest.hex())
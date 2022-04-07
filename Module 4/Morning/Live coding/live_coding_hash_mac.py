"""
Live coding: Hash functions and MACs (1)
• Write a program in Python which, given some data, computes the following:
• The MD5 digest of the data
• The SHA256 digest of the data
• The HMAC-SHA256 MAC tag of the data
• Have the program print the data and the computed digests and MAC tag
• Try with some data which is plaintext, what do you observe about the digests and
MAC tag?
"""

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from os import urandom # For generating keys

# Data which we want to verify
data = b'Hello world'

# Compute MD5 digest of the data
md5hash = hashes.Hash(hashes.MD5(), default_backend())
md5hash.update(data)
md5digest = md5hash.finalize()
print("md5:", md5digest.hex())

# Compute SHA256 digest of the data
sha256hash = hashes.Hash(hashes.SHA256(), default_backend())
sha256hash.update(data)
sha256digest = sha256hash.finalize()
print("sha256:", sha256digest.hex())

# Compute HMAC-SHA256 MAC tag of the data
key = urandom(16)
mac = hmac.HMAC(key, hashes.SHA256(), default_backend())
mac.update(data)
tag = mac.finalize()
print("MAC tag:", tag.hex())

# Verify tag:
mac = hmac.HMAC(key, hashes.SHA256(), default_backend())
mac.update(data) # Same data as before
try:
    mac.verify(tag)
    print("OK")
except InvalidSignature:
    print("ERROR")

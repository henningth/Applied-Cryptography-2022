"""
Write a program in Python which computes the MAC of some given 
data and a secret key
Use HMAC in the Cryptography module
Write it as a function computeTag(m,k), which returns the tag

Add a function verifyTag(m, t, k) which takes message m, 
tag t and key k as input, and returns True or False 
depending on whether tag is valid (=not tampered with)
"""
from cryptography.hazmat.primitives import hmac, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from os import urandom

key = urandom(16)
message = b"Yellow Submarine"

def computeTag(message, key):
    h = hmac.HMAC(key, hashes.SHA256(), default_backend())
    h.update(message)
    tag = h.finalize()
    return tag

def verifyTag(message, key, tag):
    h = hmac.HMAC(key, hashes.SHA256(), default_backend())
    h.update(message)
    try:
        h.verify(tag)
        print("OK")
    except InvalidSignature:
        print("ERROR")

tag = computeTag(message, key)
print(tag.hex())

verifyTag(message, key, tag)

# Change message
message2 = b"Yellow submarine"
tag2 = computeTag(message2, key)

verifyTag(message2, key, tag2)
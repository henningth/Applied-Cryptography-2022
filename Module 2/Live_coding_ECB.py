"""
Live coding AES-ECB example from Lec. 2.
"""

# Import cryptographic algorithms
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# For key generation
from os import urandom

# Generate key
key = urandom(16)

# Create cipher object
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB(), backend=default_backend())

# Define plain text
plaintext = b'Hello AES World!'

# Encryption
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(ciphertext)

# Decryption
decryptor = cipher.decryptor()
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(decrypted_plaintext)
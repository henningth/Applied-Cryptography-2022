"""
Block ciphers
Exercise 2: Begin by encrypting a string of your own choosing 
using AES-CTR. Then, change one byte in the ciphertext, 
and try to decrypt this modified ciphertext using the 
same key as before. Does it work, and if so, what is 
the (modified?) plaintext?
Also change one byte in the key, can you decrypt 
using the modified key?
Exercise 3: Generate a random ciphertext and decrypt 
it using the same key and nonce as in the previous exercise. 
Does it work? Why/why not?
"""

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

inputString = b'UCN Aalborg'
key = urandom(16)
iv = urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CTR(iv), default_backend())

# Encrypt plaintext
encryptor = cipher.encryptor()
ciphertext = encryptor.update(inputString) + encryptor.finalize()

# Change one byte in ciphertext, and try to decrypt it
changed_ciphertext = b"\x03" + ciphertext[1:]

decryptor = cipher.decryptor()
decrypted_ciphertext = decryptor.update(changed_ciphertext) + decryptor.finalize()

print(decrypted_ciphertext)

# Generate random ciphertext, and decrypt it
random_ciphertext = urandom(len(changed_ciphertext))

decryptor = cipher.decryptor()
decrypted_random_ciphertext = decryptor.update(random_ciphertext) + decryptor.finalize()

print(decrypted_random_ciphertext)

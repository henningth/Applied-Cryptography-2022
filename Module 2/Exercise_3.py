"""
Exercise 3: Starting from the AES-ECB live coding example, 
add functions so that the user can input an arbitrary text string.
 This text string should then be encrypted, and the ciphertext 
 should be printed in the console. Be sure to check that your 
 code can decrypt the ciphertext also. (Hint: Note that the 
 code requires plaintext and ciphertext to be bytearrays.)
"""

# Import cryptographic algorithms
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# For key generation
from os import urandom

# Generate key
key = urandom(16)

# Create cipher object
cipher = Cipher(algorithm=algorithms.AES(key), mode=modes.ECB(), backend=default_backend())

# Define plain text
plaintext = input("Enter plaintext:").encode('utf-8')

# Pad the plaintext
padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plaintext) + padder.finalize()

#print(padded_plaintext)

# Encryption
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
print(ciphertext)

# Decryption
decryptor = cipher.decryptor()
decrypted_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
print(decrypted_plaintext)

# Remove padding from decrypted text
unpadder = padding.PKCS7(128).unpadder()
unpadded_plaintext = unpadder.update(decrypted_plaintext) + unpadder.finalize()

# Decode (to print æ, ø and å)
print(unpadded_plaintext.decode('utf-8'))
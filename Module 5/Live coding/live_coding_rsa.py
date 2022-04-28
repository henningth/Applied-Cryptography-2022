"""
Use the Cryptography module in Python to encrypt and decrypt data using RSA

Generate private and public keys and save them in separate PEM files using the method in the previous slides

Check that the encryption is correct

Use OAEP padding (PKCS1.5 is only for legacy)
"""

# Imports
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate private RSA key
private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

# Generate public key from private key
public_key = private_key.public_key()

# Convert to PEM before they are written to file
private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )


# Write keys to file
with open("rsa_private_key.pem", "wb") as f:
    f.write(private_pem)

with open("rsa_public_key.pem", "wb") as f:
    f.write(public_pem)

# Encrypt data using public key:
plaintext = b'This is a test'

ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(ciphertext)
# Decrypt data using private key:
decryptedtext = private_key.decrypt(
    ciphertext, 
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(decryptedtext)
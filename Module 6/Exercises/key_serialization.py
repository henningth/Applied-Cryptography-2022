"""
Generate a public and private ECC key using the curve SECP384R1.
Serialize the public key, which can then be sent over a socket connection.
Deserialize the public key, which can then be used in the program 
for subsequent cryptography tasks.
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key

# Generate server private key
server_private_key = ec.generate_private_key(ec.SECP384R1())

# Generate server public key
server_public_key = server_private_key.public_key()

# Serialize public key
serialized_public_key = server_public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

# Print serialized key
print(serialized_public_key)

# Deserialize the public key
deserialized_public_key = load_pem_public_key(serialized_public_key)
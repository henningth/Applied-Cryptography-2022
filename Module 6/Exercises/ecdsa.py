"""
Using Elliptic Curve Digital Signature Algorithm (ECDSA)
 to sign and verify some data of your own choice.
Uses the curve SECP384R1 and hash algorithm SHA256
Prints the signature in the console
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

# Generate private key
private_key = ec.generate_private_key(ec.SECP384R1())

# The message we want to sign
message = b'Message to be signed.'

# We sign the message, yielding a signature
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# Extract the public key (used for verification)
public_key = private_key.public_key()

# Print the signature
print(signature)
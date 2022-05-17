"""
Implements Elliptic Curve Diffie-Hellman key exchange in Python using the Cryptography library
Uses https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/#elliptic-curve-key-exchange-algorithm 
Prints the shared secret in the console
Compare with the ”standard” Diffie-Hellman key exchange (diffie_hellman.py).
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Generate Alice's private key and corresponding public key
private_key_alice = ec.generate_private_key(ec.SECP384R1())
public_key_alice = private_key_alice.public_key()

# Generate Bob's private key and corresponding public key
private_key_bob = ec.generate_private_key(ec.SECP384R1())
public_key_bob = private_key_bob.public_key()

# Generate shared key (Alice's point of view)
shared_key_alice = private_key_alice.exchange(ec.ECDH(), public_key_bob)

# Derive key for use in subsequent communication
derived_key_alice = HKDF(hashes.SHA256(), 32, None, b'Derived key from handshake').derive(shared_key_alice)

# Generate shared key (Bob's point of view)
shared_key_bob = private_key_bob.exchange(ec.ECDH(), public_key_alice)

# Derive key for use in subsequent communication
derived_key_bob = HKDF(hashes.SHA256(), 32, None, b'Derived key from handshake').derive(shared_key_bob)

# Print derived keys
print("Derived key for Alice", derived_key_alice)
print("Derived key for Bob", derived_key_bob)

# Check that the exchange succeeded
if derived_key_alice == derived_key_bob:
    print("They match.")
else:
    print("They do not match.")
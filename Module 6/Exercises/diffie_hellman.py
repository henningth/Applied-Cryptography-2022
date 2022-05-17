"""
Implements Diffie-Hellman key exchange in Python using the Cryptography library
Use https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/ 
Prints the shared secret in the console
"""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

# Generate parameters for the Diffie Hellman key exchange
parameters = dh.generate_parameters(generator=2, key_size=1024, backend=default_backend)

# Generate Alice's private key and corresponding public key
private_key_alice = parameters.generate_private_key() # a
public_key_alice = private_key_alice.public_key() # A

# Generate Alice's private key and corresponding public key
private_key_bob = parameters.generate_private_key() # b
public_key_bob = private_key_bob.public_key() # B

# Generate shared key (Alice's point of view)
shared_key_alice = private_key_alice.exchange(public_key_bob)

# Derive key for use in subsequent communication
derived_key_alice = HKDF(hashes.SHA256(), 32, None, b'Derived key from handshake').derive(shared_key_alice)

# Generate shared key (Bob's point of view)
shared_key_bob = private_key_bob.exchange(public_key_alice)

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
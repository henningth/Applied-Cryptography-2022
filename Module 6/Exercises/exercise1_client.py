"""
Solution for exercise 1 (client part of key exchange 
over a socket connection).
"""

import socket
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

# Generate client's private key
client_private_key = ec.generate_private_key(ec.SECP384R1())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print("Connected to: ", (host, port))

    # Derive public key
    client_public_key = client_private_key.public_key()

    # Serialize the public key before sending it
    serialized_public_key = client_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    
    # Send the serialized public key to the ser ver
    s.send(serialized_public_key)

    # Receive server's serialized public key
    serialized_server_public_key = s.recv(1024)

    # Deserialize server's public key
    server_public_key = serialization.load_pem_public_key(serialized_server_public_key)

    # Get shared key
    client_shared_key = client_private_key.exchange(ec.ECDH(), server_public_key)
    
    # Derive shared secret
    derived_shared_key = HKDF(hashes.SHA256(), 32, None, b'Server shared key').derive(client_shared_key)
    print(derived_shared_key)
    
    # In the below loop, actual data is 
    # exchanged between server and client.
    # (exercise 3)
    """
    while True:
        s_data = input("Enter data to send: ")
        s.sendall(s_data.encode())
        r_data = s.recv(1024)
        print('Received', r_data)
    """
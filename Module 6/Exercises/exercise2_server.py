"""
Solution for exercise 2 (server part of key exchange 
over a socket connection).
"""

import socket
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes

host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

# Generate server's private key
server_private_key = ec.generate_private_key(ec.SECP384R1())

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by:", addr)
        
        # Receive public key from client
        serialized_client_public_key = conn.recv(1024)

        # Deserialize the client's public key
        client_public_key = serialization.load_pem_public_key(serialized_client_public_key)

        # Send server's public key to client
        server_public_key = server_private_key.public_key()

        # Serialize the key and send it
        serialized_server_public_key = server_public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        conn.send(serialized_server_public_key)

        # Get shared key
        server_shared_key = server_private_key.exchange(ec.ECDH(), client_public_key)
        
        # Derive shared secret
        derived_shared_key = HKDF(hashes.SHA256(), 32, None, b'Server shared key').derive(server_shared_key)
        print(derived_shared_key)

        # In the below loop, actual data is 
        # exchanged between server and client.
        # (exercise 3)
        """
        while True:
            r_data = conn.recv(1024)
            if not r_data:
                break
            print("Data received: ", r_data)
            s_data = input("Enter data to send: ")
            conn.sendall(s_data.encode())
        """
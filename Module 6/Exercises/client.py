"""
Client script for the client-server chat program
"""

import socket

host = '127.0.0.1'  # The server's hostname or IP address
port = 12345        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print("Connected to: ", (host, port))

    # Add your code here for the key exchange
    # (exercise 1)
    
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
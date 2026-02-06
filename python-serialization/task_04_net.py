#!/usr/bin/env python3
"""
Task 4: Client-Server Application with Serialization
"""
import socket
import json


def start_server():
    """
    Start a simple server that listens for JSON data, deserializes it,
    and prints it.
    """
    host = 'localhost'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    # print(f"Server listening on {host}:{port}")

    try:
        client_socket, addr = server_socket.accept()
        # print(f"Connection from {addr}")

        data = client_socket.recv(1024).decode('utf-8')
        if data:
            received_dict = json.loads(data)
            print("Received Dictionary from Client:")
            print(received_dict)
            
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()
        server_socket.close()


def send_data(data):
    """
    Send a dictionary to the server serialized as JSON.

    Args:
        data (dict): The dictionary to send.
    """
    host = 'localhost'
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        serialized_data = json.dumps(data)
        client_socket.send(serialized_data.encode('utf-8'))
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()

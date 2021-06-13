import socket
import threading
import os
from typing import Any


def accept_client() -> Any:
    while True:
        # append multiple client connection and listen to broadcast server
        client_socket, client_address = ser_sock.accept()
        CONNECTION_LIST.append(client_socket)
        thread_client = threading.Thread(target=broadcast_user, args=[client_socket])
        thread_client.start()


def broadcast_user(connected_user: socket.socket) -> Any:
    while True:
        # receive a broadcast message from user
        try:
            data = connected_user.recv(1024)
            if data:
                broadcast_buffer(connected_user, data)
        except Exception as x:
            print(x)
            os._exit(0)


def broadcast_buffer(connected_client: socket.socket, msg: Any) -> Any:
    # send buffered message to broadcast server
    for client in CONNECTION_LIST:
        if client != connected_client:
            client.send(msg)


if __name__ == "__main__":
    # initialize connection and prepare for broadcasting
    CONNECTION_LIST = []
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = '127.0.0.1'
    PORT = 5023
    ser_sock.bind((HOST, PORT))
    ser_sock.listen(1)
    print('Server listening on port : ' + str(PORT))
    thread_ac = threading.Thread(target=accept_client)
    thread_ac.start()

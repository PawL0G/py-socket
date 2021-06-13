import socket
import threading
import os
from datetime import datetime
from typing import Any


def send() -> Any:
    while True:
        # send message after user input some data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S ")
        msg = input('\nMessage: ')
        data = f'Event from {socket.gethostbyname(socket.gethostname())}: ' + msg + '\n'
        if msg == 'exit' or msg == 'exit()':
            os._exit(0)
        with open('data.txt', 'a') as the_file:
            the_file.write(dt_string + f'Event from {socket.gethostbyname(socket.gethostname())}: ' + msg + '\n')
        cli_sock.send(bytes(data, 'utf-8'))


def receive() -> Any:
    while True:
        # receive message from broadcast server '127.0.0.1'
        data = cli_sock.recv(1024)
        print('\t' + str(data))


if __name__ == "__main__":
    # initialize client connection
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5023

    cli_sock.connect((host, port))
    print('Connected to localhost...')

    thread_send = threading.Thread(target=send)
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()
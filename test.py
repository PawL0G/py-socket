import logging
import socket

logger = logging.getLogger(__name__)


def is_socket_alive(sock: socket.socket, host: str, port: int) -> bool:
    try:
        sock.connect((host, port))
        data = sock.recv(16)
        print(data)
        if len(data) == 0:
            return True

    except BlockingIOError:
        return False

    except ConnectionResetError:
        return True

    except Exception as e:
        logger.exception("unexpected exception when checking if a socket is closed")
        return False
    return False


is_socket_alive(socket.socket(socket.AF_INET, socket.SOCK_STREAM), '127.0.0.1', 5023)

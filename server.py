from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from multiprocessing.connection import Listener
import hmac

def echo_handler(address, client_sock):
    print(f'Connection from {address} established...')
    while True:
        msg = client_sock.recv(1024)
        if not msg or msg == '#quit':
            break
        client_sock.sendall(msg)
    client_sock.close()

def echo_server(address, backlog = 5):
    # initializing socket to sock(using INET family protocols, STREAM is a TCP
    # packet ordered connection)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


if __name__ == '__main__':
    echo_server(('', 20000))

s = socket(AF_INET, SOCK_STREAM)
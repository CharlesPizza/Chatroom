from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread 
from queue import Queue

clients = []
nicknames = []
def broadcast(msg):
    for client in clients:
        client.send(msg)

def client_handler(q):
    sock, client_addr = q.get()
    clients.append(sock)
    sock.send(b'Enter Nickname: ')
    nickname = sock.recv(1024) +b': '
    print(f'{nickname} connected...')
    while True:
        msg = sock.recv(1024)
        if not msg:
            break
        msg = nickname + msg
        broadcast(msg)
        
    sock.close()

def server(addr, nworkers):
    # Initialize Queue Object for communication between preallocated threads
    q = Queue()
    # prespawn worker threads manually
    for n in range(nworkers):
        t = Thread(target=client_handler, args = (q,))
        t.start()

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(addr)
        s.listen(5)
        while True:
            client_sock, client_addr = s.accept()
            q.put((client_sock, client_addr))

host = 'localhost'
port = 20000

server((host, port), 16)
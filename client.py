from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread 
from queue import Queue 
host = 'localhost'
port = 20000
def read_msg():
    while True:
        msg = c.recv(1024)
        print(msg.decode())
        print('>')
    c.close()

def write_msg():
    while True:
        msg = input('>')
        if msg == '!quit':
            c.close()
        c.send(msg.encode())

with socket(AF_INET, SOCK_STREAM) as c:
    c.connect((host, port))
    q = Queue()
    read_thread = Thread(target=read_msg, name='read')
    write_thread = Thread(target=write_msg, name='write')
    read_thread.start()
    write_thread.start()
    while True:
        pass
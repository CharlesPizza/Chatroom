from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing.connection import Listener
import hmac 
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
msg = s.recv(1024)


while True:
    print("Message:", msg)
    inmsg = s.recv(1024)
    outmsg = input("...")
    s.send(outmsg)
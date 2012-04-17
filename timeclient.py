#!/usr/bin/env python
from socket import *

HOST='10.66.129.8'
PORT=9527
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpclsock = socket(AF_INET, SOCK_STREAM)
tcpclsock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpclsock.send(data)
    data = tcpclsock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpclsock.close()

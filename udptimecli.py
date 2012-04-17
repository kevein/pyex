#!/usr/bin/env python

from socket import *

HOST = '10.66.129.8'
PORT = 3371
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpclisock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpclisock.sendto(data, ADDR)
    data, ADDR = udpclisock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

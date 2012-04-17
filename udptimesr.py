#!/usr/bin/env python

from socket import *
from time import ctime

HOST = '10.66.129.8'
PORT = 3371
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpsvsock = socket(AF_INET, SOCK_DGRAM)
udpsvsock.bind(ADDR)

try:
    while True:
        print 'waiting for message...'
        data, addr = udpsvsock.recvfrom(BUFSIZ)
        udpsvsock.sendto('[%s] %s' % (ctime(), data), addr) 
        print '...received from and returned to:', addr
except (EOFError, KeyboardInterrupt):
    udpsvsock.close()

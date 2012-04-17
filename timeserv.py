#!/usr/bin/env python
from socket import *
from time import ctime
PORT=9527
BUFSIZ = 1024
HOST = '10.66.129.8'
ADDR = (HOST, PORT)
tcpsvsock = socket()
tcpsvsock.bind(ADDR)
tcpsvsock.listen(5)

try:
    while True:
        print 'waiting for conn...'
        tcpclsock, addr= tcpsvsock.accept()
        print '..connected from:', addr
    
        while True:
            data = tcpclsock.recv(BUFSIZ)
            if not data:
                break
            tcpclsock.send('[%s] %s' % (ctime(), data))
            print data
    
        tcpclsock.close()
except (EOFError, KeyboardInterrupt):        
    tcpsvsock.close()

#! /usr/bin/env python3
"""A One Hour One Life decoder/encoder server, recives messages from the client and
passes them to bot code that allows for packet injection and packet reading"""

import select
import oholparser as parser
import socket
import time


TIME_WAIT = 0.01
BIND_ADDR = ''
BIND_PORT = 8006
SERV_ADDR = 'server1.onehouronelife.com'
SERV_PORT = 8005


def Route():
    myparser = parser.Parser()
    listener = socket.socket()
    listener.bind((BIND_ADDR, BIND_PORT))
    listener.listen(1)
    client, caddr = listener.accept()
    listener.close()
    server = socket.socket()
    server.connect((SERV_ADDR, SERV_PORT))
    running = True
    while running:
        try:
            rlist = select.select([client, server], [], [])[0]
            if client in rlist:
                stream = b""
                buf = b" "
                while buf != b"":
                    buf = client.recv(4096)
                    stream += buf
                buf = stream
                myparser.parsepacket(buf.decode("ascii"))
                if len(buf) == 0:
                    running = False
                server.send(buf)
            if server in rlist and running:
                stream = b""
                buf = b" "
                while buf != b"":
                    buf = server.recv(4096)
                    stream += buf
                buf = stream
                myparser.parsepacket(buf.decode("ascii"))
                if len(buf) == 0:
                    running = False
                client.send(buf)
        except:
            pass
    try:
        client.close()
    except:
        pass
    try:
        server.close()
    except:
        pass
    return myparser.parsed



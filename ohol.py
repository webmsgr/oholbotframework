#! /usr/bin/env python3
"""A One Hour One Life decoder/encoder server, recives messages from the client and
passes them to bot code that allows for packet injection and packet reading"""
import traceback
import select
import oholparser as parser
import socket
import time
import sys

TIME_WAIT = 0.01
BIND_ADDR = ''
BIND_PORT = 8006
SERV_ADDR = 'server1.onehouronelife.com'
SERV_PORT = 8005
# @todo add hooks for packet injection/modifing
def Route():
    myparser = parser.Parser()
    listener = socket.socket()
    listener.bind((BIND_ADDR, BIND_PORT))
    listener.listen(1)
    client, caddr = listener.accept()
    print(caddr)
    listener.close()
    server = socket.socket()
    server.connect((SERV_ADDR, SERV_PORT))
    running = True
    client.setblocking(1)
    server.setblocking(1)
    
    while running:
        try:
            rlist = select.select([client, server], [], [])[0]
            if client in rlist:
                buf = client.recv(4096)
                if len(buf) == 0:
                    running = False
                print("S <-- {}".format(buf))
                myparser.parsepacket(buf)
                server.send(buf)

            if server in rlist and running:
                buf = server.recv(4096)
                if len(buf) == 0:
                    running = False
                # Parse, modify, or halt traffic here
                print("C <-- {}".format(buf))
                myparser.parsepacket(buf)
                client.send(buf)
        except Exception as e:
            traceback.print_exception(*sys.exc_info())
            running = False
    client.close()
    server.close()
    return myparser.parsed

packets = Route()

#! /usr/bin/env python3
"""A One Hour One Life decoder/encoder server, recives messages from the client and
passes them to bot code that allows for packet injection and packet reading"""
import traceback
import select
import oholparser as parser
import socket
import time
import sys
import multiprocessing as mp # oh no
import threading # its multiprocessing/threading time!
TIME_WAIT = 0.01
BIND_ADDR = ''
BIND_PORT = 8006
SERV_ADDR = 'server1.onehouronelife.com'
SERV_PORT = 8005

def themanager(serversocket,clientsocket):
    server,s = mp.Pipe()
    client,c = mp.Pipe()
    serverThread = threading.Thread(target=Server,args=(s,serversocket))
    clientThread = threading.Thread(target=Server,args=(c,clientsocket))
    clientThread.start()
    serverThread.start()
    parsingserver = []
    parsingclient = []
    with mp.Pool(processes=4) as pool:
        while serverThread.is_alive() and clientThread.is_alive():
            if server.poll():
                data = server.recv()
                if data == b"": continue
                print("C <-- {}".format(data))
                parsingclient.append(pool.apply_async(messageWorker,(data,)))
            if client.poll():
                data = client.recv()
                if data == b"": continue
                print("S <-- {}".format(data))
                parsingserver.append(pool.apply_async(messageWorker,(data,)))
            while parsingserver != [] and parsingserver[0].ready():
                server.send(parsingserver.pop(0).get())
            while parsingclient != [] and parsingclient[0].ready():
                client.send(parsingclient.pop(0).get())
        
        
        
def passthrough(packets,direction):
    return packets
def messageWorker(message):
    return message
def Server(pipe,msocket):
    msocket.setblocking(0)
    while True:
        try:
            read,write,_  = select.select([msocket],[msocket],[],60)
            if msocket in read:
                buf = msocket.recv(2048)
                pipe.send(buf)
            if pipe.poll() and msocket in write:
                msocket.send(pipe.recv())
        except:
            break
            
def Route(func=passthrough):
    myparser = parser.Parser()
    listener = socket.socket()
    listener.bind((BIND_ADDR, BIND_PORT))
    listener.listen(1)
    client, caddr = listener.accept()
    print(caddr)
    listener.close()
    server = socket.socket()
    server.connect((SERV_ADDR, SERV_PORT))
    themanager(server,client)
    client.close()
    server.close()
if __name__ == "__main__":
    pass
    #Route()

"""A One Hour One Life decoder/encoder server, recives messages from the client and
passes them to bot code that allows for packet injection and packet reading"""

cdef extern from "<stdio.h>" nogil:
    int sscanf   (const char *s, const char *template, ...)
cdef extern from "<stdlib.h>" nogil:
    int atoi (const char* str)
cdef extern from "<string.h>" nogil:
    char *strstr (const char *s1, const char *s2);
    void *memcpy  (void *pto, const void *pfrom, size_t size)
cdef LiveObject Player
cpdef GridPos gridpos(int x, int y):
    cdef GridPos gri
    gri.x = x
    gri.y = y
    return gri

cdef ClientMessage parseMessage(LiveObject inplayer, char *inMessage):
    cdef char* nameBuffer
    cdef char* atpos
    cdef ClientMessage m
    cdef int numRead = 0
    cdef int offset
    offset = 3
    cdef int numTokens
    cdef int i
    m.i = -1
    m.c = -1
    m.id = -1
    m.trigger = -1
    m.numExtraPos = 0
    m.extraPos = NULL
    m.saidText = NULL
    m.bugText = NULL
    m.sequenceNumber = -1
    cdef int parselength = <int>len(inMessage)
    if parselength > 99:
        parselength = 99
    for i in range(parselength):
        if inMessage[i] == b' ':
            if numRead == 0:
                if i != 0:
                    mes = inMessage[:i]
                    nameBuffer = mes
                    nameBuffer[i] = b"\0"
                    numRead += 1
                    i -= 1
            elif numRead == 1:
                m.x = atoi( &( inMessage[i] ) )
                numRead += 1
            elif numRead == 2:
                m.y = atoi( &( inMessage[i] ) )
                numRead += 1


    print(nameBuffer)
    if <bytes>nameBuffer == b"MOVE":
        m.type = MOVE
        strmessage = (<bytes>inMessage).decode()
        strmessageu = strmessage[strmessage.find("@"):]
        atpos = <char *>strmessageu
        if strmessage.find("@") != -1:
            offset = 4
        tokens = strmessage.split()
        if ( len(tokens) < offset + 2 or ( len(tokens) - offset ) % 2 != 0 ):
            m.type = UNKNOWN
            return m
        if strmessage.find("@") != -1:
            m.sequenceNumber = <int>int(tokens[3][1])
        numTokens = len(tokens)




cpdef parseMess(name,message):
    cdef LiveObject Player
    Player.name = <char *>name
    mes = parseMessage(Player,<char *>message)
    return mes.type



import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8006            # Arbitrary non-privileged port
outHOST = 'server1.onehouronelife.com'    # The remote host
outPORT = 8005              # The same port as used by the server

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                ss.connect((outHOST, outPORT))
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    ss.sendall(data)
                    data = ss.recv(1024)
                    if not data: break
                    conn.sendall(ss)

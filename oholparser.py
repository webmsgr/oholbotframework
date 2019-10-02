"""Parse client/server packets into a object and allow converting from the object to a packet"""
class Parser():
    def __init__(self):
        self.parsed = []
    def parsepacket(self,packet):
        # @todo fix packet parser
        # @body a new implemtation would allow for the parsing of map chunks and compressed messages, both of which show up as two packets
        packets = packet.split(b"#")
        if packets[0] == packet:
            rawpacket = packet
            packet = packet.split()
            packet = [x for x in packet if x != b""]
            if packet != []:
                packetobj = packobj.get(packet[0].strip(),UnknownPacket)()
                packetobj.parse(packet,rawpacket)
                self.parsed.append(packetobj)
        else:
            [self.parsepacket(x) for x in packets if x.strip() != ""]
# @todo add more packet types to parser
class BasePacket:
    def __init__(self,direction):
        self.direct = direction
        self.type = "BASE"
        self.data = ""
    def parse(self,args,raw): # takes the raw packet and populates itself
        self.data = raw
    def packet(self): # takes self and converts it to a packet
        return self.data
class UnknownPacket(BasePacket):
    def __init__(self):
        super().__init__("?")
        self.type = "UNKNOWN"
    def parse(self,args,raw):
        self.data = raw

class Frame(BasePacket):
    def __init__(self):
        super().__init__("c") # send to client
        self.type = "FRAME"
    def packet(self):
        return "FM\n#"
class Shutdown(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "SHUTDOWN"
    def parse(self,data,raw):
        self.playercount = data[1]
        self.data = raw
class Server_full(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "SERVER_FULL"
    def parse(self,data,raw):
        self.playercount = data[1]
        self.data = raw
class ServerLogin(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "SERVER_LOGIN"
    def parse(self,data,raw):
        self.playercount = data[1]
        self.challengestring = data[2]
        self.version = data[3]
        self.data = raw
class Accepted(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "ACCEPTED"
    def parse(self,data,raw):
        self.data = raw
class Rejected(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "REJECTED"
    def parse(self,data,raw):
        self.data = raw
class No_life_tokens(Rejected):
    def __init__(self):
        super().__init__()
        self.type = "REJECTED_NO_LIFE_TOKENS"
    def parse(self,data,raw):
        self.data = raw
class Login(BasePacket):
    def __init__(self):
        super().__init__("s")
        self.type = "CLIENT_LOGIN"
    def parse(self,data,raw):
        self.email,self.password_hash,self.account_key_hash,self.tutorial_number = data[1:5]
        self.twins = False
        self.data = raw
        if len(data) > 5:
            self.twin_code_hash = data[5]
            self.twin_count = data[6]
            self.twins = True
class PlayerInfo(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "PLAYERINFO"
    def parse(self,data,rawdata):
        self.data = rawdata
        self.players = []
        for player in rawdata.split(b"\n")[1:]:
            self.players.append(player.split(b" "))
class PlayerSaid(BasePacket):
    def __init__(self):
        super().__init__("c")
        self.type = "PLAYER_SAID"
    def parse(self,data,rawdata):
        tokens = rawdata.split("\n")[1:]
        self.data = rawdata
        self.messages = []
        for token in tokens:
            self.messages.append(token.split(" "))

packobj = {b"FM":Frame,
            b"SHUTDOWN":Shutdown,
            b"SERVER_FULL":Server_full,
            b"SN":ServerLogin,
            b"ACCEPTED":Accepted,
            b"REJECTED":Rejected,
            b"NO_LIFE_TOKENS":No_life_tokens,
            b"LOGIN": Login,
            b"PU": PlayerInfo,
            b"PS": PlayerSaid
            }

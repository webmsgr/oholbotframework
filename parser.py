"""Parse client/server packets into a object and allow converting from the object to a packet"""
class Parser():
    def __init__(self):
        self.serverfeed = []
        self.clientfeed = []
        self.parsedserver = []
        self.parsedclient = []
    def parsepacket(self,packet,direction):
        packets = packet.split("#")
        if packets[0] == packet:
            packet = packet.split("\n")
            packet = [x for x in packet if x.strip() != ""]
            packetobj = packobj.get(packet[0],UnknownPacket)()
            packetobj.parse(packet)
            if direction == "s":
                self.parsedserver.append(packetobj)
            else:
                self.parsedclient.append(packetobj)
        else:
            [self.parsepacket(x,direction) for x in packets if x.strip() != ""]
class BasePacket:
    def __init__(self,direction):
        self.direct = direction
        self.type = "BASE"
    def parse(self,args): # takes the raw packet and populates itself
        pass
    def packet(self): # takes self and converts it to a packet
        pass
class UnknownPacket(BasePacket):
    def __init__(self):
        super().__init__("?")
        self.type = "UNKNOWN"
    def parse(self,args):
        self.data = args

class Frame(BasePacket):
    def __init__(self):
        super().__init__("c") # send to client
        self.type = "FRAME"
    def packet(self):
        return "FM\n#"
packobj = {"FM":Frame}

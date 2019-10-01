"""Parse client/server packets into a object and allow converting from the object to a packet"""
class Parser():
    def __init__(self):
        self.serverfeed = []
        self.clientfeed = []
        self.parsedserver = []
        self.parsedclient = []
class BasePacket():
    def __init__(self,direction)
        self.direct = direction
    def parse(self,args): # takes the raw packet and populates itself
        pass
    def packet(self): # takes self and converts it to a packet
        pass
class Frame(BasePacket):
    def __init__(self):
        super().__init__("c") # send to client
    def packet(self):
        return "FM\n#"
packobj = {"FM":Frame}

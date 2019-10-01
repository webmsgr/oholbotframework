"""Parse client/server packets into a object and allow converting from the object to a packet"""

class Parser():
    def __init__(self):
        self.serverfeed = []
        self.clientfeed = []
        self.parsedserver = []
        self.parsedclient = []
class BasePacket():
    def __init__(self,rawpacket,direction)
        self.rawpacket = rawpacket
        self.direct = direction
class Frame(BasePacket):
    def __init__(self):
        super().__init__("FM\n#","c") # send to client
        

"""A One Hour One Life decoder/encoder server, recives messages from the client and 
passes them to bot code that allows for packet injection and packet reading"""


cdef struct s_GridPos:
    int x
    int y
ctypedef s_GridPos GridPos

ctypedef enum messageType:
    MOVE,
    USE,
    SELF,
    BABY,
    UBABY,
    REMV,
    SREMV,
    DROP,
    KILL,
    SAY,
    EMOT,
    JUMP,
    DIE,
    GRAVE,
    OWNER,
    FORCE,
    MAP,
    TRIGGER,
    BUG,
    PING,
    VOGS,
    VOGN,
    VOGP,
    VOGM,
    VOGI,
    VOGT,
    VOGX,
    PHOTO,
    UNKNOWN
cdef struct s_ClientMessage:
        messageType type
        int x, y, c, i, id
        int trigger
        int bug
        # some messages have extra positions attached
        int numExtraPos
        #NULL if there are no extra
        GridPos *extraPos
        # null if type not SAY
        char *saidText       
        # null if type not BUG
        char *bugText
        # for MOVE messages
        int sequenceNumber
ctypedef s_ClientMessage ClientMessage

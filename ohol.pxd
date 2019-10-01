
ctypedef struct GridPos:
        int x
        int y
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
ctypedef struct ClientMessage:
        messageType type;
        int x, y, c, i, id
        int trigger
        int bug
        int sequenceNumber
        int numExtraPos
        GridPos *extraPos
        char *saidText
        char *bugText


ctypedef struct LiveObject:
        char *email
        char *origEmail
        int id
        float fitnessScore
        int displayID
        char *name
        char nameHasSuffix
        char *familyName
        char *lastSay
        int curseTokenCount
        char curseTokenUpdate
        char isEve
        char isTutorial
        char isTwin
        GridPos birthPos
        GridPos originalBirthPos
        int parentID
        int parentChainLength
        int lineageEveID
        double lifeStartTimeSeconds
        double deathTimeSeconds
        double trueStartTimeSeconds
        double lastSayTimeSeconds
        double firstEmoteTimeSeconds
        int emoteCountInWindow
        char emoteCooldown
        double emoteCooldownStartTimeSeconds
        char heldByOther
        int heldByOtherID
        char everHeldByParent
        int responsiblePlayerID
        int killPosseSize
        int xs
        int ys
        int xd
        int yd
        char posForced
        char waitingForForceResponse
        int lastMoveSequenceNumber
        int pathLength
        GridPos *pathToDest
        char pathTruncated
        char firstMapSent
        int lastSentMapX
        int lastSentMapY
        GridPos mapChunkPathCheckedDest
        double moveTotalSeconds
        double moveStartTime
        double pathDist
        int facingOverride
        int actionAttempt
        GridPos actionTarget
        int holdingID
        char heldOriginValid
        int heldOriginX
        int heldOriginY
        int heldGraveOriginX
        int heldGraveOriginY
        int heldGravePlayerID
        int heldTransitionSourceID
        int numContained
        int *containedIDs
        int embeddedWeaponID
        int murderSourceID
        char holdingWound
        int murderPerpID
        char *murderPerpEmail
        int deathSourceID
        char everKilledAnyone
        char suicide
        char gotPartOfThisFrame
        char isNew
        char firstMessageSent
        char inFlight
        char dying
        double dyingETA
        char emotFrozen
        double emotUnfreezeETA
        int emotFrozenIndex
        char connected
        char error
        const char *errorCauseString
        int customGraveID
        char *deathReason
        char deleteSent
        double deleteSentDoneETA
        char deathLogged
        char newMove
        float heatMap[ 13 * 13 ]
        float envHeat
        float bodyHeat
        float biomeHeat
        float lastBiomeHeat
        float heat
        char heatUpdate
        double lastHeatUpdate
        char isIndoors
        int foodStore
        double foodCapModifier
        double fever
        double foodDecrementETASeconds
        char foodUpdate
        int lastAteID
        int lastAteFillMax
        char justAte
        int justAteID
        int yummyBonusStore
        char needsUpdate
        char updateSent
        char updateGlobal
        double playerCrossingCheckTime
        char monumentPosSet
        GridPos lastMonumentPos
        int lastMonumentID
        char monumentPosSent
        char holdingFlightObject
        char vogMode
        GridPos preVogPos
        GridPos preVogBirthPos
        int vogJumpIndex
        char postVogMode

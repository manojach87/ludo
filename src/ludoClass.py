colors = {0: "red", 1: "green", 2: "yellow", 3: "blue"}
highwayStartLoc = {0: 0, 1: 13, 2: 26, 3: 39}
highwayHomeStartLoc = {0: 51, 1: 58, 2: 64, 3: 70}


class gatti:
    color = -1
    loc = -1
    gattiId = 0
    gattiCount = 0
    inSafeZone = True
    safeZones = [-1, 0, 8, 13, 21, 26, 34, 39, 47]
    homeZones = [51, 52, 53, 54, 55, 56]

    def __init__(self, color):
        self.color = color
        self.loc = -1
        # self.gattiCount = gatti.gattiCount
        # gatti.gattiCount+=1
        gatti.gattiId += 1
        self.gattiId = gatti.gattiId

    def isInSafeZone(self):
        if (self.loc in self.safeZones):
            return (True)
        else:
            return (False)

    def move(self, numMoves):
        if (numMoves == 6 & self.loc == -1):
            # print("In Here")
            self.loc == 0
        elif(self.loc + numMoves ):
            self.loc = self.loc + numMoves
        inSafeZone = self.isInSafeZone()


class startZone:
    # This the class for the 4 start Zones i.e. for all the colors
    # 4 Gatti for each color
    items = 0
    color = -1
    # gattis=dict({0:set(),1:set(),2:set(),3:set()})
    gattis = set()
    for color in colors:
        i = 0
    for i in range(4):
        gattis.add(gatti(color))

    startZoneCount = 0

    # Create statZone with 4 Gatti
    def __init__(self, color):
        self.color = color
        self.items = 4
        #        if(startZone.startZoneCount<=4):

        while len(self.gattis) < 4:
            x = gatti(color)

            # self.gattis[color].add(gatti(color))
            # print(x)
            self.gattis.add(x)
        # print("{} : {}".format(x,x.color))

    #            startZone.startZoneCount+=1

    def addGatti(self, gattiObj):
        if (self.items < 4):
            self.gattis.add(gattiObj)
            self.items += 1

    def removeGatti(self):
        if (self.items > 0):
            self.items -= 1
            return (self.gattis.pop())

    @classmethod
    def getGattis(self, color):
        gattis = set()
        for gatti in startZone.gattis:
            print(gatti)
            if (gatti.color == color):
                gattis.add(gatti)


class homeZone:
    items = 0
    gattis = set()

    def __init__(self, color):
        self.color = color

    def addGatti(self, gattiObj):
        self.items += 1
        self.gattis.add(gattiObj)

    def removeGatti(self, color):
        self.items -= 1
        return (self.gattis.pop())

x=startZone(0)
#y=startZone(0)

for item in x.gattis:
    print(item)

#for item in y.gattis:
#    print(item)


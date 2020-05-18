colors = {0: "red", 1: "green", 2: "yellow", 3: "blue"}
## This class is for the gatti
class gatti:
    loc = -1
    MAXMOVES = 56
    inSafeZone = True
    SAFEZONES = [-1, 0, 8, 13, 21, 26, 34, 39, 47]
    HOMEZONES = [51, 52, 53, 54, 55, 56]

    def __init__ (self,color):
        self.color = color
        self.loc = -1

    def move(self,numMoves):
        # If the gatti is at its start position
        if(self.loc < 0 ):
            # Gatti needs a 6 to move out from start position
            if(numMoves==6):
                print("Its a six!")
                self.loc+=1
            # Do nothing if its not a six
            else:
                print("Its not a six! Still Stuck!")
                #self.loc+=numMoves
        # if it is not a six
        elif (self.loc + numMoves <= gatti.MAXMOVES):
            self.loc = self.loc + numMoves
        else:
            print("here")
            #pass

        #inSafeZone=self.isInSafeZone()


class startZone:
    allGattis = {
        "red": set(),
        "blue": set(),
        "green": set(),
        "yellow": set()
    }
    def __init__(self,players):
        self.players=players
        for i in self.allGattis:
            pass
            #print(self.allGattis[i])

        for color in self.players:
            for i in range(4):
               #print("{}".format(allGattis[colors[color]]))
                self.allGattis[colors[color]].add(gatti(color))
                #print("{} {}".format(i,k))

    def checkOtherGattis(self,gatti):
        for color in self.players:
            if(color != gatti.color):
                for otherGatti in self.allGattis[colors[color]]:
                    if(otherGatti.loc==gatti.loc):
                        print(otherGatti.color)
                        otherGatti.loc=-1



                    #print("{} {}".format(i,k))
        #if(self.players)



import random as random

class ludoWorld:

    def __init__(self,numPlayers):
        self.players=random.sample(colors.keys(), numPlayers)
        print(self.players)
        self.startZone = startZone(self.players)
        self.turn=self.players.pop()

    def decideTurn(self):
        self.players.append(self.turn)
        self.turn=self.players.pop()

    def chooseGattiToPlay(self,gatti):
        gatti=gatti()
        random.randint(1,4)

    def moveGatti(self):
        moves=random.randint(1,6)
        #moves = 6
        self.playerColor = colors[self.turn]
        for j in self.startZone.allGattis[colors[self.turn]]:
            j.move(moves)
            self.startZone.checkOtherGattis(j)
    def showGattiStatus(self):
        for i in self.startZone.allGattis:
            print(i)#len(self.startZone.allGattis[i]))
            for j in self.startZone.allGattis[i]:
                print(j.loc)


x=ludoWorld(2)
x.moveGatti()
x.showGattiStatus()


# for i, k in enumerate(colors):
#     print(k)
# i=random.randint(1,6)
# while (i!=6):
#     i=random.randint(1,6)
#     print(i)


# red=gatti(0)
# print(red.loc)
# red.move(5)
# print(red.loc)

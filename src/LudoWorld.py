#from ludo import StartZone, Gatti
from StartZone import StartZone
from Gatti import Gatti
import random as random


class LudoWorld:
    ABS_POS={"red":0,"green":13,"yellow":26,"blue":39}
    MAX_MOVES_OUT=50
    def __init__(self, numPlayers):
        self.playerColors = random.sample(Gatti.colors.keys(), numPlayers)
        print(self.playerColors)

        self.startZone = StartZone(self.playerColors)
        #print(self.startZone)

        self.turn = self.playerColors.pop()
        self.playerColors.append(self.turn)

        print(self.turn)
    ## WHo gets the next turn
    def decideTurn(self):
        self.turn = self.playerColors.pop()
        self.playerColors.append(self.turn)

    def chooseGattiToPlay(self, gatti):
        gatti = gatti()
        return (random.randint(1, 4))

    def moveGatti(self):
        moves = random.randint(1, 6)
        # moves = 6
        self.playerColor = Gatti.colors[self.turn]

        for j in self.startZone.allGattis[Gatti.colors[self.turn]]:
            j.move(moves)
            self.startZone.checkOtherGattis(j)

    def moveGatti1(self, gattiObj):
        moves = random.randint(1, 6)
        # moves = 6
        self.playerColor = Gatti.colors[self.turn]
        gattiObj.move(moves)
        self.startZone.checkOtherGattis(gattiObj)

    def showGattiStatus(self):
        for i in self.startZone.allGattis:
            print(i)  # len(self.startZone.allGattis[i]))
            for j in self.startZone.allGattis[i]:
                print(j.loc)



from StartZone import StartZone
from Gatti import Gatti
import random as random


class LudoWorld:

    def __init__(self, numPlayers):
        self.players = random.sample(Gatti.colors.keys(), numPlayers)
        print(self.players)

        self.startZone = StartZone(self.players)
        print(self.startZone)

        self.turn = self.players.pop()
        print(self.turn)

    def decideTurn(self):
        self.players.append(self.turn)
        self.turn = self.players.pop()

    def chooseGattiToPlay(self, gatti):
        gatti = gatti()
        random.randint(1, 4)

    def moveGatti(self):
        moves = random.randint(1, 6)
        # moves = 6
        self.playerColor = Gatti.colors[self.turn]
        for j in self.startZone.allGattis[Gatti.colors[self.turn]]:
            j.move(moves)
            self.startZone.checkOtherGattis(j)

    def showGattiStatus(self):
        for i in self.startZone.allGattis:
            print(i)  # len(self.startZone.allGattis[i]))
            for j in self.startZone.allGattis[i]:
                print(j.loc)

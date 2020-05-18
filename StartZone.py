from Gatti import Gatti


class StartZone:
    # suru garney game ko color haru lai
    # always start with two players
    allGattis = {
        "red": set(),
        "blue": set(),
        "green": set(),
        "yellow": set()
    }

    def __init__(self, players):
        # choose how many players to play
        self.players=players
        for i in self.allGattis:
            pass
            #print(self.allGattis[i])

        # assin gatti of different color to the player
        for color in self.players:
            for i in range(4):
               #print("{}".format(allGattis[colors[color]]))
                self.allGattis[Gatti.colors[color]].add(Gatti(color))
                #print("{} {}".format(i,k))

    def checkOtherGattis(self, gatti):
        for color in self.players:
            if(color != gatti.color):
                for otherGatti in self.allGattis[Gatti.colors[color]]:
                    if(otherGatti.loc==gatti.loc):
                        print(otherGatti.color)
                        otherGatti.loc=-1



                    #print("{} {}".format(i,k))
        #if(self.players)


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

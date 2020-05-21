#from ludo import LudoWorld
from LudoWorld import  LudoWorld
from Gatti import  Gatti
#from LudoWorld import LudoWorld


x = LudoWorld(3)
colorNum=x.playerColors[0]
colorDesc=Gatti.colors[colorNum]
gatti=x.startZone.allGattis[colorDesc].copy().pop()

print(x.startZone.allGattis[colorDesc])
print(gatti)
x.moveGatti1(gatti)
x.showGattiStatus()

print(x.playerColors)
def getAbsLoc(gatti):
    colorNum=gatti.color
    loc=gatti.loc
    colorDesc = Gatti.colors[colorNum]
    absLoc=loc
    if(loc>=0):
        absLoc+=LudoWorld.ABS_POS[colorDesc]
    return(absLoc)
    # for colorNum in x.playerColors:
    #     colorDesc = Gatti.colors[colorNum]
    #
    #     print(LudoWorld.ABS_POS[colorDesc])

print(getAbsLoc(gatti))
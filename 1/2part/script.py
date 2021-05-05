import math


def getFuel(mass):
     return int(math.floor(int(mass)/3-2))

f = open('input.txt','r')
#print(f.read())


totalFuel = 0
for mMass in f:
    tempFuel = getFuel(mMass)
    moduleFuel = 0
    while tempFuel > 0:
        moduleFuel += tempFuel
        tempFuel = getFuel(tempFuel)
    totalFuel += moduleFuel




print(totalFuel)

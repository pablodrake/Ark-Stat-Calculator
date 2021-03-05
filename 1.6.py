import random
import pyinputplus as pyip
from timeit import default_timer as time

minLimit = 1
maxLimit = 1
relativeProb = 0
stat = 0
iterationNumber = 0
average = 0
bonusLvl = 0
loopCounter = 1
isSim = 0


wild = pyip.inputYesNo("Is it a wild animal? Yes/No ")
flyers = pyip.inputYesNo("Is it a flyer? Yes/No ")
if wild == "N" or wild == "no" or wild == "No" or wild == "no":
    wildLvl = int(pyip.inputNum("Level of the animal before being tamed "))
    tamedLvl = int(pyip.inputNum("Level of the animal after being tamed ", greaterThan=wildLvl))
    beforestatLvl = int(pyip.inputNum("Level of the stat before being tamed "))
    statLvl = int(pyip.inputNum("Level of the stat after being tamed ", greaterThan=beforestatLvl))
    tries = int(pyip.inputNum("Number of iterations "))
    lvl = tamedLvl - wildLvl
    if lvl == 1:
        lvl = 2
    statLvl = statLvl - beforestatLvl
else:
    wildLvl = int(pyip.inputNum("Level of the animal ", greaterThan=1))
    statLvl = int(pyip.inputNum("Level of the stat you want to calculate "))
    tries = int(pyip.inputNum("Number of iterations "))
    lvl = wildLvl


def simulation(minlimit, maxlimit):
    stat = 0
    for i in range(1, lvl):
        if random.randint(minlimit, maxlimit) == 1:
            stat += 1
    return stat


tic = time()

while iterationNumber < tries:
    stat = 0
    relativeProb = 0
    while stat < statLvl:
        if flyers == "Y" or flyers == "y" or flyers == "Yes" or flyers == "yes":
            stat = simulation(1, 6)
        else:
            stat = simulation(1, 7)

        relativeProb += 1
    iterationNumber += 1
    average = average + relativeProb
    relativePos = (1 / relativeProb)*100
    print("Value in success:", stat)
    print("Relative probability:", end=" ")
    print(relativePos, "%", sep="")
    print("Number of tries:", relativeProb)
    print("Iteration number:", iterationNumber)
    print("======================================")

toc = time()
totalProb = ((1 / (average / iterationNumber))*100)
avgTries = average / iterationNumber
print("Total number of simulations:", iterationNumber)
print("Average number of tries:", avgTries)
print("Total probability of success:", end=" ")
print(totalProb, "%", sep="")
print("Elapsed time is", toc-tic, "seconds")

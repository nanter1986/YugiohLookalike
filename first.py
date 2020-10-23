import random
from player import Player
from cardMaker import Card

playerReal=Player()
playerCom=Player()

def printGap():
    print("-------------------")


def display_situation():
    print("You:")
    print(playerReal.display_situation())
    printGap()
    print("Com:")
    print(playerCom.display_situation())

def coinToss():
    pass

def theLoop():
    while playerReal.life>0 and playerCom.life>0:
        #handCurrent=[Card(),Card(),Card()]


display_situation()

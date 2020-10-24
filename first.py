import random
from player import Player
from cardMaker import Card

playerReal=Player()
playerCom=Player()
realPlayerTurn=True;

def printGap():
    print("-------------------")


def display_situation():
    print("You:")
    print(playerReal.displayPlayer())
    printGap()
    print("Com:")
    print(playerCom.displayPlayer())

def coinToss():
    print("Coin Toss")
    realPlayerTurn=random.choice((True,False))
    if realPlayerTurn==True:
        print("Your Turn")
    else:
        print("Com Turn")


def theLoop():
    while playerReal.life>0 and playerCom.life>0:
        if realPlayerTurn==True:
            print("Your Turn")
            handCurrent=[
                    Card(),
                    Card(),
                    Card(),
                    Card(),
                    Card()
                    ]
            for c in handCurrent:
                print(str(handCurrent.index(c)+1)+"...")
                c.display_card()

            input("What")
            realPlayerTurn==False
        else:
            print("Com Turn")

            realPlayerTurn==True


display_situation()
coinToss()
theLoop()

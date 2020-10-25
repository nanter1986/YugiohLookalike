import random
from player import Player
from cardMaker import Card

playerReal = Player()
playerCom = Player()
realPlayerTurn = True


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
    realPlayerTurn = random.choice((True, False))
    if realPlayerTurn:
        print("Your Turn")
    else:
        print("Com Turn")


def theLoop():
    global realPlayerTurn
    while playerReal.life > 0 and playerCom.life > 0:
        if realPlayerTurn:
            print("Your Turn")
            handCurrent = [
                    Card(),
                    Card(),
                    Card(),
                    Card(),
                    Card()
                    ]
            for c in handCurrent:
                print(str(handCurrent.index(c)+1)+"...")
                c.display_card()

            input_selection = input("Choose Card Indexes")
            check_if_cost_of_selection_within_limits(handCurrent,
                                                     input_selection)
            realPlayerTurn = False
        else:
            print("Com Turn")

            realPlayerTurn = True


def check_if_cost_of_selection_within_limits(hand_current, input_selection):
    cost = 0
    for s in input_selection:
        c = hand_current[int(s)-1].cost
        cost = cost+c
    print("Total cost:"+str(cost))
    if cost <= playerReal.force:
        print("valid cost")
    else:
        print("invalid cost")


display_situation()
coinToss()
theLoop()

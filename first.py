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

            the_input=get_input_check_validity()
            check_if_cost_of_selection_within_limits(handCurrent,
                                                     the_input)
            realPlayerTurn = False
        else:
            print("Com Turn")

            realPlayerTurn = True


def get_input_check_validity():
    length_valid = False
    value_valid = False
    duplication_valid=False
    input_selection=0
    while value_valid == False or length_valid == False:
        input_selection = input("Choose Card Indexes")
        print("length:"+str(len(input_selection)))
        if len(input_selection) < 6:
            length_valid = True
        value_valid = True
        for s in input_selection:
            if int(s) > 5:
                value_valid = False
        if length_valid == False:
            print("incorrect length")
        if value_valid == False:
            print("incorrect value")
    return input_selection


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

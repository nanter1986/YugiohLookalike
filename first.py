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

            the_input = get_input_check_validity()
            print("the input from the function:"+the_input)
            correct_input = check_if_cost_of_selection_within_limits(
                handCurrent,
                the_input)
            print("correct input returned:"+str(correct_input))
            playerField = move_selected_cards_to_field(the_input, handCurrent)
            field_after_combiner_check = check_if_field_contains_combiner(
                playerField)
            realPlayerTurn = False
        else:
            print("Com Turn")

            realPlayerTurn = True


def check_if_field_contains_combiner(playerField):
    new_player_field = None
    new_combined_card = None
    length_of_field = len(playerField)
    should_combine = False
    for c in playerField:
        if c.combiner == 1:
            should_combine = True
    if should_combine == True:
        list_of_cards_to_combined_card(playerField)
    else:
        new_player_field = playerField
    return new_player_field


def list_of_cards_to_combined_card(list):
    card_attack = 0
    card_attribute = None
    card_exploder = 0
    card_combiner = 0
    card_summoner = 0
    card_booster = 0
    list_of_attributes = []
    for c in list:
        card_attack = card_attack+c.att
        if c.summoner == 1:
            card_summoner = 1
        if c.combiner == 1:
            card_combiner = 1
        if c.exploder == 1:
            card_exploder = 1
        if c.booster == 1:
            card_booster = 1
        list_of_attributes.append(c.attr)
    decide_attribute_for_combined_card(list_of_attributes)


def decide_attribute_for_combined_card(list_of_attributes):
    pass


def move_selected_cards_to_field(correct_input, handCurrent):
    print("correct input"+str(correct_input))
    print("hand current"+str(handCurrent))
    playerField = []
    selections = []
    for s in correct_input:
        selections.append(int(s)-1)
    for i in selections:
        playerField.append(handCurrent[i])
    for c in playerField:
        c.display_card()
    return playerField


def get_input_check_validity():
    length_valid = False
    value_valid = False
    duplication_valid = False
    contains_zero_valid = False
    input_selection = ""
    print("input selection before the loop:"+input_selection)
    while value_valid == False\
            or length_valid == False\
            or duplication_valid == False\
            or contains_zero_valid == False:
        input_selection = input("Choose Card Indexes")
        # check length
        print("length:"+str(len(input_selection)))
        if len(input_selection) < 6:
            length_valid = True
        # check value above five
        value_valid = True
        for s in input_selection:
            if int(s) > 5:
                value_valid = False
        # check if value contains zero
        contains_zero_valid = True
        for s in input_selection:
            if int(s) == 0:
                contains_zero_valid = False
        if length_valid == False:
            print("incorrect length")
        if value_valid == False:
            print("incorrect value")
        if len(set(input_selection)) == len(input_selection):
            duplication_valid = True
            print("no duplicates")
        else:
            print("duplicate found")
        if contains_zero_valid == False:
            print("contains zero")
    print("out of the loop,validation successful")
    print("output selection out of the loop:"+input_selection)
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

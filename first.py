import random
from player import Player
from cardMaker import Card

playerReal = Player()
playerCom = Player()
realPlayerTurn = True
turn_count=0


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
    global turn_count
    while playerReal.life > 0 and playerCom.life > 0:
        if realPlayerTurn:
            turn_count=turn_count+1
            print("Turn:"+str(turn_count))
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
            display_list_of_cards(field_after_combiner_check)
            do_battle_if_not_the_first_turn(turn_count)
            realPlayerTurn = False
        else:
            print("Com Turn")
            print("Turn:"+str(turn_count))

            realPlayerTurn = True

def do_battle_if_not_the_first_turn(count):
    if turn_count==0:
        print("cant battle on 1st turn")
    else:
        print("battle begins...")


def display_list_of_cards(the_list):
    for c in the_list:
        print(str(the_list.index(c)+1)+"...")
        c.display_card()


def check_if_field_contains_combiner(playerField):
    new_player_field = None
    new_combined_card = None
    length_of_field = len(playerField)
    should_combine = False
    for c in playerField:
        if c.combiner == 1:
            should_combine = True
    if should_combine == True:
        new_player_field = list_of_cards_to_combined_card(playerField)
    else:
        new_player_field = playerField
    return new_player_field


def list_of_cards_to_combined_card(list):
    list_to_return = []
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
    the_attribute = decide_attribute_for_combined_card(list_of_attributes)
    the_made_card = Card(att=card_attack,
                         attr=the_attribute,
                         combiner=card_combiner,
                         summoner=card_summoner,
                         exploder=card_exploder,
                         booster=card_booster)
    list_to_return.append(the_made_card)
    return list_to_return


def decide_attribute_for_combined_card(list_of_attributes):
    dark_count = 0
    light_count = 0
    fire_count = 0
    water_count = 0
    earth_count = 0
    wind_count = 0
    for c in list_of_attributes:
        if c == "DARK":
            dark_count = dark_count+1
        if c == "LIGHT":
            light_count = light_count+1
        if c == "FIRE":
            fire_count = fire_count+1
        if c == "WATER":
            water_count = water_count+1
        if c == "EARTH":
            earth_count = earth_count+1
        if c == "WIND":
            wind_count = wind_count+1
    made_list = [dark_count,
                 light_count,
                 fire_count,
                 water_count,
                 earth_count,
                 wind_count
                 ]
    the_max_value = max(made_list)
    the_highest_counted_attributes = []
    if dark_count == the_max_value:
        the_highest_counted_attributes.append("DARK")
    if light_count == the_max_value:
        the_highest_counted_attributes.append("LIGHT")
    if fire_count == the_max_value:
        the_highest_counted_attributes.append("FIRE")
    if water_count == the_max_value:
        the_highest_counted_attributes.append("WATER")
    if earth_count == the_max_value:
        the_highest_counted_attributes.append("EARTH")
    if wind_count == the_max_value:
        the_highest_counted_attributes.append("WIND")
    the_choosen_attribute = random.choice(the_highest_counted_attributes)
    return the_choosen_attribute


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

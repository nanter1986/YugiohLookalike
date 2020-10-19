import random

def attributeAssigner():
    all=("DARK","LIGHT","EARTH","WIND","FIRE","WIND")
    attribute=random.choice(all)
    return attribute

def card_maker():
    card=[]
    att=random.randint(0,10)
    card.append(att)
    attr=attributeAssigner()
    card.append(attr)
    exploder=random.randint(0,1)
    card.append(exploder)
    returner=random.randint(0,1)
    card.append(returner)
    reborner=random.randint(0,1)
    card.append(reborner)
    drawer=random.randint(0,1)
    card.append(drawer)
    print(str(card))



def printGap():
    print("-------------------")


def display_situation():
    print("Player Life:")
    print("100")
    print("Player Force:")
    print("50")
    printGap()
    print("Com Life:")
    print("100")
    print("Com Force:")
    print("50")

display_situation()
for i in range(0,5):
    card_maker()

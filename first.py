import random
from cardMaker import Card


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
    c=Card()
    c.display_card()

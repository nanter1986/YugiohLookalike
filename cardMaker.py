import time
import colorama
from colorama import Fore, Back, Style
import random

colorama.init(autoreset=True)


class Card:
    def __init__(self):
        self.att = random.randint(0, 10)
        self.attr = self.attributeAssigner()
        self.exploder = random.randint(0, 1)
        self.combiner = random.randint(0, 1)
        self.summoner = random.randint(0, 1)
        self.booster = random.randint(0, 1)
        self.cost = self.calculateCost()
        # print(str(self))
        # calculateCost()

    def attributeAssigner(self):
        all = ("DARK", "LIGHT", "EARTH", "WIND", "FIRE", "WIND")
        attribute = random.choice(all)
        return attribute

    def display_card(self):
        print("------------------")
        print("ATT:"+str(self.att))
        print("ATR:"+self.attr)
        if self.exploder == 1:
            print(Fore.RED+"EXPLODER")
        if self.combiner == 1:
            print(Fore.BLUE+"COMBINER")
        if self.summoner == 1:
            print(Fore.YELLOW+"SUMMONER")
        if self.booster == 1:
            print(Fore.GREEN+"BOOSTER")
        print("COST:"+str(self.cost))

        print("------------------")
        time.sleep(1)

    def calculateCost(self):
        a = self.att*10
        s = self.summoner*10
        b = self.booster*10
        e = self.exploder*10
        c = self.combiner*10
        cost = a+s+b+e+c

        return cost

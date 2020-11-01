import time
import colorama
from colorama import Fore, Back, Style
import random

colorama.init(autoreset=True)


class Card:
    def __init__(self, att=None,
                 attr=None,
                 exploder=None,
                 summoner=None,
                 booster=None,
                 combiner=None):
        if att is None:
            self.att = random.randint(0, 10)
        else:
            self.att = att
        if attr is None:
            self.attr = self.attributeAssigner()
        else:
            self.attr = attr
        if exploder is None:
            self.exploder = random.randint(0, 1)
        else:
            self.exploder == exploder
        if combiner is None:
            self.combiner = random.randint(0, 1)
        else:
            self.combiner = combiner
        if summoner is None:
            self.summoner = random.randint(0, 1)
        else:
            self.summoner = summoner
        if booster is None:
            self.booster = random.randint(0, 1)
        else:
            self.booster = booster
        self.cost = self.calculateCost()

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

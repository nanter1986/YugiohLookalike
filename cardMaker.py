import colorama
from colorama import Fore, Back, Style
import random

colorama.init(autoreset=True)

class Card:
    def __init__(self):    
        self.att=random.randint(0,10)
        self.attr=self.attributeAssigner()
        self.exploder=random.randint(0,1)
        self.returner=random.randint(0,1)
        self.summoner=random.randint(0,1)
        self.drawer=random.randint(0,1)
        print(str(self))
        #calculateCost()

    def attributeAssigner(self):
        all=("DARK","LIGHT","EARTH","WIND","FIRE","WIND")
        attribute=random.choice(all)
        return attribute

    def display_card(self):
        print("------------------")
        print("ATT:"+str(self.att))
        print("ATR:"+self.attr)
        if self.exploder==1:
            print(Fore.RED+"EXPLODER")
        if self.returner==1:
            print(Fore.BLUE+"RETURNER")
        if self.summoner==1:
            print(Fore.YELLOW+"SUMMONER")
        if self.drawer==1:
            print(Fore.GREEN+"DRAWER")
        print("------------------")

    def calculateCost(self):
        pass




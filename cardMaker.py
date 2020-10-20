import random

class Card:
    def __init__(self):    
        self.att=random.randint(0,10)
        self.attr=self.attributeAssigner()
        self.exploder=random.randint(0,1)
        self.returner=random.randint(0,1)
        self.reborner=random.randint(0,1)
        self.drawer=random.randint(0,1)
        print(str(self))

    def attributeAssigner(self):
        all=("DARK","LIGHT","EARTH","WIND","FIRE","WIND")
        attribute=random.choice(all)
        return attribute

    def display_card(self):
        print("------------------")
        print("ATT:"+str(self.att))
        print("ATR:"+self.attr)
        if self.exploder==1:
            print("EXPLODER")
        if self.returner==1:
            print("RETURNER")
        if self.reborner==1:
            print("REBORNER")
        if self.drawer==1:
            print("DRAWER")
        print("------------------")




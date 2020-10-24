class Player():
    def __init__(self):
        self.life=100
        self.force=100

    def displayPlayer(self):
        print(str(self.life)
                +"/"
                +str(self.force))



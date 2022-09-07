from player import Player


import random
class AI:
    def __init__(self) :
        super().__init__()
        pass

    def choose_gesture(self):
        self.selection = str(random.radiant(0,4))
        if self.human.selection == 0:
            print ("Rock has been choosen")
        elif self.human.seleciton ==1:
            print ("Paper has been choosen")
        elif self.human.seleciton ==2:
            print("Scissors has been choosen")
        elif self.human.seleciton ==3:
            print ("Lizard has been choosen")
        elif self.human.seleciton ==4:
            print ("Spock has been choosen")
               
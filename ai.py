from player import Player
from time import sleep

import random
class AI(Player):
    def __init__(self) :
        super().__init__()
        self.score = 0
        self.name = ""
        pass

    def choose_gesture(self):
        self.selection = str(random.radiant(0,4))
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep(1)
        print (f"{self.name} has picked {gesture_list [int(self.selection)]}")
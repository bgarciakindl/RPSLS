from player import Player
from time import sleep
import random
class AI(Player):
    def __init__(self) :
        super().__init__()
        self.name = ""
        self.score = 0
        

    def choose_gesture(self):
        self.random_gesture = str(random.randint(0,4))
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]

        sleep(1)
        self.selected_gesture = gesture_list [int(self.random_gesture)]
        print (f"Player has picked {self.selected_gesture}")
        return self.selected_gesture
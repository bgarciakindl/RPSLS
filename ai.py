from player import Player
from time import sleep
import random
class AI(Player):
    def __init__(self) :
        super().__init__()
        self.name = ""
        self.score = 0
        

    def choose_gesture(self):
        self.gesture = str(random.randint(0,4))
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep(1)
        print (f"Player has picked {gesture_list [int(self.gesture)]}")
        return self.gesture
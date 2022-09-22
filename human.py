
from calendar import c
from player import Player

from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.score = 0
        
#make sure it stor
    def choose_gesture(self):
        self.user_gesture = input("Please select a gesture (0)Rock,(1)Paper,(2)Scissors,(3)Lizard,(4)Spock: ")
        
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep(1)
        self.selected_gesture = gesture_list [int(self.user_gesture)]
        print (f"Player has picked {self.selected_gesture}")
        return self.user_gesture

    
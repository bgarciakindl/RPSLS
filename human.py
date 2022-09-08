
from calendar import c
from player import Player

from time import sleep

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = ""
        

    def choose_gesture(self):
        self.selection = input("Please select a gesture (0)Rock,(1)Paper,(2)Scissors,(3)Lizard,(4)Spock: ")
        gesture_list = ["Rock","Paper","Scissors","Lizard","Spock"]
        sleep(1)
        print (f"Player has picked {gesture_list [int(self.selection)]}")

    
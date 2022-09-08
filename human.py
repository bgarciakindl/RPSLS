from operator import truediv
from player import Player

from time import sleep

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.name = ""
        pass

    def choose_gesture(self):
        gesture_selected = input("Please select a gesture (0)Rock,(1)Paper,(2)Scissors,(3)Lizard,(4)Spock: ")
        self.selection = gesture_selected
        print (f"{self.name} has picked {self.selection}")
        
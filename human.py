from player import Player
import random
from time import sleep

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        pass

    def choose_gesture(self):
        self.selection = input("Please select a gesture: ")

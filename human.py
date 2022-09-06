from player import Player

from time import sleep

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        pass

    def choose_gesture(self):
        print(self.gesture_list)
        self.selection = input("Please select a gesture: ")


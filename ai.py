from player import Player


import random
class AI:
    def __init__(self) :
        super().__init__()
        pass

    def choose_gesture(self):
        self.selection = str(random.radiant(0,4))
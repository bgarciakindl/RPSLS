from operator import truediv
from player import Player

from time import sleep

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        pass

    def choose_gesture(self,valid_selection):
        valid_selection == False
        print(self.human_gesture_list)
        sleep(1)
        self.human.selection = input("Please select a gesture (0)Rock,(1)Paper,(2)Scissors,(3)Lizard,(4)Spock: ")
        while valid_selection == False:
            if self.human.selection == 0:
                print ("You have chosen Rock")
                valid_selection == True
            elif self.human.seleciton ==1:
                print ("You have chosen Paper")
                valid_selection == True
            elif self.human.seleciton ==2:
                print("You have chosen Scissors")
                valid_selection == True
            elif self.human.seleciton ==3:
                print ("You have chosen Lizard")
                valid_selection == True
            elif self.human.seleciton ==4:
                print ("You have chosen Spock")
                valid_selection == True
            else:
                print ("You have not choosen a valid option please select again")




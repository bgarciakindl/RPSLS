import imp
from socket import AI_CANONNAME
from time import sleep
from human import Human
from ai import AI


class Game:
    def __init__(self) -> None:
        pass

    def run_games(self):
        self.print_rules()
        self.player_selection()
        self.play_game()   
    
    def print_rules (self): 
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (1)
        
    def player_selection (self,player_one,player_two):
        player_number= input("Please Select the number of human players 1 or 2 or 3 for a surprise: ")
        if player_number == 1:
            player_one = Human
            player_two = AI
        elif player_number == 2:
            player_one = Human
            player_two = Human
        else:
            player_one = AI
            player_two = AI
        
        return player_one,player_two
    
    def play_game(self):
        pass
    #compare values and add to the score of the winner compare gesture seclection and declare a winner
    #build one game for multi player and single
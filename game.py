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
    
    def print_rules (self): 
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (.5)
    
    def player_selection(self,player_number,player_one,player_two):
        player_number= input("Please Select the number of human players 1 or 2 or 3 for a surprise: ")
        if player_number == 1:
            player_one = human_one
            player_two = ai_one
        elif player_number == 2:
            player_one = human_one
            player_two = human_two
        else:
            player_one = ai_one
            player_two = ai_two
        
        return player_number

    
    def play_game (self):
      pass
    
    def display_winner():
        pass
    #compare values and add to the score of the winner compare gesture seclection and declare a winner
    #build one game for multi player and single
from time import sleep
from human import Human
from ai import AI
from player import Player


class Game:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

    def run_games(self):
        self.print_rules()
        self.player_selection()
        self.play_game() 
        self.declare_winner()
        self.play_again()
    
    def print_rules (self): 
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (1)
        #if elif else broke and is no longer recognizing inputs no need third option need three things how to define them and get the routine need them name 
    def player_selection (self):
        player_number= input("Please Select the number of players 1 or 2 or 3 for quick view of the game: ")
        if player_number == 1:
            player_one= Human("player 1")
            player_two = AI("player 2")
            print ("You have selected to go against the computer")
        elif player_number == 2:
           player_one = Human ("player 1")
           player_two = Human ("player 2")
           print ("You have selected to go against another human")
        elif player_number == 3:
            player_one = AI("player 1")
            player_two = AI("player 2")
            print ("You have selected to watch 2 computers play for testing purposes")
        else:
            print ("Please select one of the available options")
        
    #needs an else in the above statement
    def play_game(self):
        #see if this can be condensed so it isn't as long
        #initialize the players scores outside the while loop double check the names
        #could I just go from the player selection into the game and not have it go into a seperate function in the run game function that way it gets called immediatly
        self.player_one.score = 0
        self.player_two.score = 0
        while self.player_one.score < 2 & self.player_two.score < 2:
            player_one_gesture = self.player_one.choose_gesture()
            player_two_gesture = self.player_two.choose_gesture()
            if player_one_gesture == "Rock":
                if player_two_gesture == "Scissors" or player_two_gesture == "Lizard":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif player_two_gesture == "Paper" or player_two_gesture == "Spock":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif player_one_gesture == "Paper":
                if player_two_gesture == "Rock" or player_two_gesture == "Spock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif player_two_gesture == "Scissors" or player_two_gesture == "Lizard":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif player_one_gesture == "Scisors":
                if player_two_gesture == "Paper" or player_two_gesture == "Lizard":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif player_two_gesture == "Rock" or player_two_gesture == "Spock":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif player_one_gesture == "Lizzard":
                if player_two_gesture == "Scissors" or player_two_gesture == "Spock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif player_two_gesture == "Rock" or player_two_gesture == "Scissors":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            else:
                if player_two_gesture == "Scissors" or player_two_gesture == "Rock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif player_two_gesture == "Paper" or player_two_gesture == "Lizzard":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")

    def declare_winner(self):
        if self.player_one.score ==2:
            print ("Player One has Won")
        elif self.player_two.score == 2:
            print ("Player Two has Won")
        else:
            print ("There is no score there has been an error")
        
    def play_again(self):
        answer_equals = input("Do you wish to play again: (y/n): ") 
        if answer_equals == "y":
           self.run_games() 
        else:
            print("Thank you for playing!")
    
    #compare values and add to the score of the winner compare gesture seclection and declare a winner
    #build one game for multi player and single
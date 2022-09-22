from time import sleep
from human import Human
from ai import AI
from player import Player


class Game:
    def __init__(self):
        self.player_one = Human ()
        self.player_two = AI ()

    def run_games(self):
        self.print_rules()
        self.player_selection(self.player_one,self.player_two)
        while self.player_one.score < 2 and self.player_two.score < 2:
            if self.player_one.score == 2:
                print ("Player One Wins")
            elif self.player_two.score == 2:
                print ("Player Twon Wins")
            else:
                self.play_game() 
        self.declare_winner()
        self.play_again()
    
    def print_rules (self):
    
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (.2)
        
    def player_selection (self,player_one,player_two):
        
        player_number= input("Please Select the number of players 1 or 2 or 3 for quick view of the game: ")
        
        if player_number == "Paper":
            self.player_one= Human()
            self.player_two = AI()
            print ("You have selected to go against the computer")
        elif player_number == "2":
           self.player_one = Human ()
           self.player_two = Human ()
           print ("You have selected to go against another human")
        elif player_number == "3":
            self.player_one = AI()
            self.player_two = AI()
            print ("You have selected to watch 2 computers play for testing purposes")
        else:
            print ("Please select one of the available options")
        return self.player_one,self.player_two
    
    def play_game(self):
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.selected_gesture == "Rock":
                if self.player_two.selected_gesture == "Scissors" or self.player_two.selected_gesture == "Lizard":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif self.player_two.selected_gesture == "Paper" or self.player_two.selected_gesture == "Spock":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif self.player_one.selected_gesture == "Paper":
                if self.player_two.selected_gesture == "Rock" or self.player_two.selected_gesture == "Spock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif self.player_two.selected_gesture == "Scissors"or self.player_two.selected_gesture == "Lizard":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif self.player_one.selected_gesture == "Scissors":
                if self.player_two.selected_gesture == "Paper" or self.player_two.selected_gesture == "Lizard":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif self.player_two.selected_gesture == "Rock" or self.player_two.selected_gesture == "Spock":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            elif self.player_one.selected_gesture == "Lizard":
                if self.player_two.selected_gesture == "Paper" or self.player_two.selected_gesture == "Spock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif self.player_two.selected_gesture == "Rock" or self.player_two.selected_gesture == "Scissors":
                    print ("Player Two Wins This Round")
                    self.player_two.score +=1
                else:
                    print ("There is no winner of the round")
            else:
                if self.player_two.selected_gesture == "Scissors"or self.player_two.selected_gesture == "Rock":
                    print ("Player One Wins This Round")
                    self.player_one.score +=1
                elif self.player_two.selected_gesture == "Paper" or self.player_two.selected_gesture == "Lizard":
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
    
   
from time import sleep
from human import Human
from ai import AI


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = AI()

    def run_games(self):
        self.print_rules()
        self.player_selection(self.player_one,self.player_two)
        self.play_game() 
        self.declare_winner()
        self.play_again()
    
    def print_rules (self): 
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (1)
        
    def player_selection (self,player_one,player_two):
        player_number= input("Please Select the number of human players 1 or 2: ")
        if player_number == 1:
            player_one.name = Human("Player One")
            player_two.name = AI ("Player Two")
        elif player_number == 2:
           player_one.name = Human("Player One")
           player_two.name = Human("Player Two")
        return player_one,player_two
    
    def play_game(self):
        while self.player_one.score < 2 & self.player_two.score < 2:
            player_one_gesture = self.player_one.choose_gesture
            player_two_gesture = self.player_two.choose_gesture
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
        else:
            print ("Player Two has Won")
        
    def play_again(self):
        answer_equals = input("Do you wish to play again: (y/n): ") 
        if answer_equals == "y":
           self.run_games() 
        else:
            print("Thank you for playing!")
    
    #compare values and add to the score of the winner compare gesture seclection and declare a winner
    #build one game for multi player and single
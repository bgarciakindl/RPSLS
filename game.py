from time import sleep


class Game:
    def __init__(self) -> None:
        pass


    
    def print_rules (self): 
        rules_of_game = ["Rock crushes Scissors","Scissors cuts Paper","Paper covers Rock","Rock crushes Lizard","Lizard poisons Spock","Spock smashes Scissors","Scissors decapitates Lizard","Lizard eats Paper","Paper disproves Spock","Spock vaporizes Rock"]
        for rule in rules_of_game:
            print(rule)
            sleep (.5)


    #compare values and add to the score of the winner compare gesture seclection and declare a winner
    #build one game for multi player and single
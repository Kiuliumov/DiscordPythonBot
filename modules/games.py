import random

class Games:
 def computer_choice():
    possible_choices = ['rock', 'paper', 'scissors']
    return random.choice(possible_choices)

 def rps(user_input):
    computer_choice = computer_choice()

    if user_input == computer_choice:
        game_result = 'draw'
    else:
        if user_input == 'rock':
            if computer_choice == 'paper':
                game_result = 'lose'
            elif computer_choice == 'scissors':
                game_result = 'win'
            else:
                game_result = 'draw'
        elif user_input == 'paper':
            if computer_choice == 'scissors':
                game_result = 'lose'
            elif computer_choice == 'rock':
                game_result = 'win'
        elif user_input == 'scissors':
            if computer_choice == 'rock':
                game_result = 'lose'
            elif computer_choice == 'paper':
                game_result = 'win'
    
    return game_result

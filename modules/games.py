import random

class Games:

 def rps(user_input):
    possible_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(possible_choices)
    game_result = 'default'
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
    
    return game_result,computer_choice
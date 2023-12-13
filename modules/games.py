import random

class Games:
     def rps(self,user_input):
        possible_choices = ['rock','paper','scissors']
        computer_choice = possible_choices[random.randint(0,2)]
        if user_input in possible_choices:
         if user_input == computer_choice:
          game_result = 'draw'

         if user_input == 'rock':
            if computer_choice == 'paper':
                 game_result = 'lose'
            elif computer_choice == 'scissors':
                 game_result = 'win'
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
        else:
          return 'Not a valid input!'
        return game_result
     
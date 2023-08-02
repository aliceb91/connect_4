import os
from game_state import GameState

game = GameState()

os.system('clear')

print("Hello! Welcome to Connect 4!", "Select a column to make your first move!",  sep="\n")

print(" - - - - Let's go! - - - - ")

game.print_grid()

while game.game_over == False:

    game.set_target_column()

    game.check_grid()

    os.system('clear')

    print(" - - - - Connect 4 - - - - ")

    game.print_grid()

    game.game_over = game.validator()

os.system('clear')

print(" - - - - Winner!!! - - - - ")

game.print_grid()

print(f"Congratulations {game.current_player['name']}, you win!")

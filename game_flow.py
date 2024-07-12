from functions import print_tf
from characters import Characters
from player import Player
from levels.level_1 import level_one
import json


player = Player()
characters = Characters.load_characters(Characters)

game_status = True
player_status = [player.current_level, player.current_chapter, player.current_check_point]

while game_status:
    print_tf(f"Should we start the game?", delay=0.01)
    player_input = input().lower()
    while player_input != 'yes' and player_input != 'exit':
        print_tf(f"Please type 'Yes' to continue or 'Exit' to close the game.", delay=0.01)
        player_input = input().lower()
        continue

    if player_input.lower() == 'exit':
        print_tf(f'Exiting game now...', delay=0.01)
        game_status = False
        break
    elif player_input.lower() == 'yes':
        if player_status[0] == 1:
            game_status = level_one(game_status=game_status, player=player)
    else:
        print_tf(player_input)
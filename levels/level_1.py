import json
from functions import print_tf

def level_one(status):
    print_tf(f'Level: {status[0]}, Chapter: {status[1]}, Checkpoint: {status[2]}')

    with open('json_files/level_1.json', 'r') as file:
        texts = json.load(file)

    print_tf('> ' * 3)
    print_tf(texts['level 1']['chapter 1']['checkpoint 1'])

    ### TODO 
    # Create mechanics to auto increment level, chapter, and checkpoints ones they are completed. 
    # Figure out how to control game_status from here. Meaning if player types 'exit' to exit the game.
    # Level function should be taking game_status, player_status, and player as arguments. 
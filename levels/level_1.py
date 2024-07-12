import json
from functions import print_tf

def level_one(game_status, player):
    player_input = ''
    while game_status:
        with open('json_files/level_1.json', 'r') as file:
            texts = json.load(file)

        # Checkpoint 1
        print_tf(texts[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'])
        player.current_check_point += 1
        player.update_player({'current_check_point':player.current_check_point})

        player_input = input('> ').lower()

        while player_input != 'exit':
            # Checkpoint 2
            print_tf(texts[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'])
            player.current_check_point += 1
            player.update_player({'current_check_point':player.current_check_point})
            player_input = input('> ').lower()

            # Checkpoint 3
            print_tf(texts[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'])
            player.current_check_point += 1
            player.update_player({'current_check_point':player.current_check_point})
            player_input = input('> ').lower()
            while player_input != 'cd /home':
                print_tf(f'Make sure to type: cd /home')
            
            break
        else:
            print_tf('Exiting the game')
            game_status = False
            break
            
        break
      
    return game_status




    ###### TODO 
    ### Create close game function. It should take player_status (level, chapter, checkpoint) as input, update player.json file and close the game.
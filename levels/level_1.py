import json
from functions import load_level_text, text_style, typewritter


def level_one(game_status, player, character):
    player_input = ''
    while game_status:
        level_1_text = load_level_text(1)

        # Checkpoint 1
        # texts.typewritter(flag='level')
        typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'], flag='level')
        player.current_check_point += 1
        player.update_player({'current_check_point':player.current_check_point})

        player_input = input('> ').lower()

        while player_input != 'exit':
            # Checkpoint 2
            typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'], flag='level')
            player.current_check_point += 1
            player.update_player({'current_check_point':player.current_check_point})
            player_input = input('> ').lower()

            # Checkpoint 3
            typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_check_point}'], flag='level')
            player.current_check_point += 1
            player.update_player({'current_check_point':player.current_check_point})
            player_input = input('> ').lower()
            while player_input != 'cd /home':
                typewritter(f'Make sure to type: cd /home')
                player_input = input('> ').lower()
            
            break
        else:
            typewritter('Exiting the game')
            game_status = False
            break
            
        break
      
    return game_status




    ###### TODO 
    ### Create close game function. It should take player_status (level, chapter, checkpoint) as input, update player.json file and close the game.
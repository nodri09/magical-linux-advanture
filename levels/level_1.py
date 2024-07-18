import json
from functions import load_level_text, text_style, typewritter


def level_one(game_status, player, character):
    player_input = ''
    while game_status:
        level_1_text = load_level_text(1)

        # Checkpoint 1
        # texts.typewritter(flag='level')
        typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_checkpoint}'], flag='level')
        player.current_checkpoint += 1
        player.update_player({'current_checkpoint':player.current_checkpoint})

        player_input = input('> ').lower()

        while player_input != 'exit':
            # Checkpoint 2
            typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_checkpoint}'], flag='level')
            player.current_checkpoint += 1
            player.update_player({'current_checkpoint':player.current_checkpoint})
            player_input = input('> ').lower()

            # Checkpoint 3
            typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_checkpoint}'], flag='level')
            print(player.current_level, player.current_chapter, player.current_checkpoint)

            player_input = input('> ').lower()
            while player_input != 'cd /home':
                typewritter(f'Make sure to type: cd /home')
                print()
                player_input = input('> ').lower()
            player.current_checkpoint += 1
            player.update_player({'current_checkpoint':player.current_checkpoint})

            # Checkpoint 4
            typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_checkpoint}'], flag='level')
            player.current_checkpoint += 1
            player.update_player({'current_checkpoint':player.current_checkpoint})
        else:
            typewritter('Exiting the game')
            game_status = False
            break
            
        break
      
    return game_status




    ###### TODO 
    ### While loop to check if player typed correct command isn't working for some reason. In addition, on each iteration of the player's command check it updates current_chapter. Check why.
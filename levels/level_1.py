import json
from functions import load_level_text, typewritter, check_exit


def level_one(game_status, player, character):
    player_input = ''
    while game_status:
        level_1_text = load_level_text(1)

        # Checkpoint 1
        # texts.typewritter(flag='level')
        typewritter(level_1_text[f'level {player.current_level}'][f'chapter {player.current_chapter}'][f'checkpoint {player.current_checkpoint}'], flag='level')
        player.current_checkpoint += 1
        player.update_player({'current_checkpoint':player.current_checkpoint})

        player_input = check_exit(input('> ').lower())
        if player_input == False:
            game_status = False
        else:
            continue

        while game_status:
        # player_input != 'exit':
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
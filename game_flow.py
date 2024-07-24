from objects import Player, Characters
from levels.level_1 import level_one
from functions import typewritter

player = Player()
# player = player.load_player()
characters = Characters.load_characters(Characters)


game_status = True
# player_status = [player.current_level, player.current_chapter, player.current_check_point]

while game_status:
    typewritter(f"Should we start the game?\n", delay=0.01)
    player_input = input().lower()
    while player_input not in ['yes', 'y'] and player_input != 'exit':
        typewritter(f"Please type 'Yes' to continue or 'Exit' to close the game.\n", delay=0.01)
        player_input = input().lower()
        continue

    if player_input.lower() == 'exit':
        typewritter(f'Exiting game now...\n', delay=0.01)
        game_status = False
        break
    elif player_input.lower() in ['yes', 'y']:
        if player.current_level == 0:
            player.current_level += 1
            player.current_chapter += 1
            player.current_checkpoint += 1
            player.update_player({"current_level": player.current_level, "current_chapter": player.current_chapter, "current_checkpoint": player.current_checkpoint})
            game_status = level_one(game_status=game_status, player=player, character=characters)
    else:
        typewritter(player_input)
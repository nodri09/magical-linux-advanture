from objects import Player, GameFlow, Level, Characters
from levels.level_1 import level_one
from functions import typewritter
from rich.console import Console
import os

console = Console()



### ToDo
# Right now, after checkpoint 3 typewritter() function gives error ('list' object has no attribute 'items') - find out why;
# Before moving forward with the story write test scenarios and test the game_flow that it works as expected.
# 
# 

def game_flow():
    player = Player()
    game = GameFlow(player)
    while game.window_status:
        typewritter("Would you like to start the game? (type 'Yes' to continue or 'Exit' to exit the game)\n")
        game.window_status = game.player_input()
        if game.window_status == False:
            continue
        typewritter("Starting the game.\n")
        if game.simplified_state == [0,0,0]:
            player.update_player_state(what='+lvl')
            player.update_player_state(what='+chp')
            player.update_player_state(what='+chck')
        else:
            player.refresh_player_state()

        level_one(Level(level_digit=1, player=player, game_flow=game))

    else:
        player.save_player()
        typewritter("Exiting the game.")
        os.system('exit')


game_flow()
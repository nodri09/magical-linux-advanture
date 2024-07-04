from game_logic import GameLogic
from text_loader import load_texts
import re
import time
import sys

texts = load_texts()
app_status = True

# Initiate game logic
logic = GameLogic()

# Load or Create Player
player_loaded = logic.load_game()
# print(player_loaded)

# Check player status
player_status = logic.player_status(player_loaded)


def typewriter_effect(text, delay=0.01):
    typing_index = 0

    while typing_index < len(text):
        if isinstance(text, list):
            text = "\n".join(text)

        match_pause = re.match(r'\{pause:(\d+(\.\d+)?)\}', text[typing_index:])
        match_input = re.match(r'\{input\}', text[typing_index:])
        match_save = re.match(r'\{save\}', text[typing_index:])
        if match_pause:
            pause_duration = int(match_pause.group(1))
            time.sleep(pause_duration)
            typing_index += match_pause.end()
        elif match_input:
            user_input = input() 
            result = logic.input_checker(player_status, user_input)
            if result == 'exit':
                return 'exit'
            typing_index += match_input.end()
        elif match_save:
            logic.save_game(player_loaded['current_chapter'], player_loaded['current_stage'], player_loaded['current_chp'], player_loaded['points'])
            typing_index += match_save.end()
        else:
            sys.stdout.write(text[typing_index])
            sys.stdout.flush()
            time.sleep(delay)
            typing_index += 1
    print()  # Ensure to print a newline at the end


def game_flow():
    game_status = True
    while game_status:
        chapter = f"chapter {player_loaded['current_chapter']}"
        stage = f"stage {player_loaded['current_stage']}"
        checkpoint = f"checkpoint {player_loaded['current_chp']}"
        
        if chapter in texts and stage in texts[chapter] and checkpoint in texts[chapter][stage]:
            text = texts[chapter][stage][checkpoint]
            result = typewriter_effect(text)
        
            if result == 'exit':
                game_status = False
                break
            else:
                # Move to the next checkpoint
                player_loaded['current_chp'] += 1
                # Save the new game state
                logic.save_game(player_loaded['current_chapter'], player_loaded['current_stage'], player_loaded['current_chp'], player_loaded['points'])
        else:
            print("Invalid game state. Exiting...")
            break
    
    print("You have exited the game")

game_flow()

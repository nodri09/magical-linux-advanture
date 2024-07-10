import time
import re
import sys

def print_tf(*texts, delay=0.05):
    typing_index = 0

    for text in texts:
        if type(text) == str or type(text) == list:
            while typing_index < len(text):
                if isinstance(text, list):
                    text = "\n".join(text)

                match_pause = re.match(r'\{pause:(\d+(\.\d+)?)\}', text[typing_index:])
                # match_save = re.match(r'\{save\}', text[typing_index:])
                if match_pause:
                    pause_duration = int(match_pause.group(1))
                    time.sleep(pause_duration)
                    typing_index += match_pause.end()
                # elif match_save:
                #     logic.save_game(player_loaded['current_chapter'], player_loaded['current_stage'], player_loaded['current_chp'], player_loaded['points'])
                #     typing_index += match_save.end()
                else:
                    sys.stdout.write(text[typing_index])
                    sys.stdout.flush()
                    time.sleep(delay)
                    typing_index += 1
        else:
            print(text, end="")
        print()
import time
import re
import sys
import json
from rich.console import Console

console = Console()

def load_level_text(level):
    level_path = f'json_files/level_{level}.json'

    with open(level_path, 'r') as file:
        level_text = json.load(file)

    return level_text

def text_style(tag):

    if 'Lenny' in tag :
        style = "bold green3"
    elif 'Story' in tag:
        style = "italic grey50"
    
    return style

def typewritter(text, flag='',delay=0.05):
    try:
        if flag == 'level':
            for line, values in text.items():
                
                typing_index = 0
                while typing_index < len(values):
                    match_pause = re.match(r'\{pause:(\d+(\.\d+)?)\}', values[typing_index:])
                    if match_pause:
                        pause_duration = float(match_pause.group(1))
                        time.sleep(pause_duration)
                        typing_index += match_pause.end()
                    else:
                        console.print(values[typing_index], end='', style=text_style(line))
                        sys.stdout.flush()
                        time.sleep(delay)
                        typing_index += 1
            return True
        else:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
    except Exception as e:
        print(f'Error occured while trying typewritter effect: {e}')


# something = texts.typewritter(f"Should we start the game?")
# if something == True:
#     print('something was true')

# load_text = load_level_text(1)
# print(load_text)

# typewritter(load_text['level 1']['chapter 1']['checkpoint 2'], flag='level')
import json
from functions import typewritter
from levels.level_1 import level_one
import time
# import time
# import re

# from rich.console import Console


### PLAYER ###
class Player:
    def __init__(self) -> None:
        self.player_data = self.load_player()
        self.current_level = self.player_data['current_level']
        self.current_chapter = self.player_data['current_chapter']
        self.current_checkpoint = self.player_data['current_checkpoint']
        self.state = [self.current_level, self.current_chapter, self.current_checkpoint]

        self.completed_levels = []
        self.completed_chapters = []
        self.completed_checkpoints = []

        self.hp = 100
        self.mp = 0
        self.name = ''
        self.mastered_spells = []

    def load_player(self):
        try:
            with open('json_files/player_data.json', 'r') as file:
                player_data = json.load(file)
            self._load_from_dict(player_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading player data: {e}", delay=0.01)
            player_data = self.create_player()
            print(f"Player created", delay=0.01)
        return player_data

    def create_player(self):
        player_data = {
            "current_level": self.current_level,
            "current_chapter": self.current_chapter,
            "current_checkpoint": self.current_checkpoint,
            "completed_levels": self.completed_levels,
            "completed_chapters": self.completed_chapters,
            "completed_checkpoints": self.completed_checkpoints,
            "hp": self.hp,
            "mp": self.mp,
            "name": self.name,
            "mastered_spells": self.mastered_spells
        }
        self._save_to_file(player_data)
    
    def update_player(self, what=''):

        if what == '+lvl':
            self.player_data['current_level'] += 1
        elif what == '-lvl':
            self.player_data['current_level'] -= 1
        elif what == '+chp':
            self.player_data['current_chapter'] += 1
        elif what == '-chp':
            self.player_data['current_chapter'] -= 1
        elif what == '+chck':
            self.player_data['current_checkpoint'] += 1
        elif what == '-chck':
            self.player_data['current_checkpoint'] += 1

        self._save_to_file(self.player_data)
        self.load_player()
        self.state

    def _save_to_file(self, data):
        try:
            with open('json_files/player_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving player data: {e}")

    def _load_from_dict(self, data):
        self.current_level = data.get('current_level', None)
        self.current_chapter = data.get('current_chapter', None)
        self.current_checkpoint = data.get('current_checkpoint', None)

        self.completed_levels = data.get('completed_levels', None)
        self.completed_chapters = data.get('completed_chapters', None)
        self.completed_check_points = data.get('completed_check_points', None)

        self.hp = data.get('hp', None)
        self.mp = data.get('mp', None)
        self.name = data.get('name', None)
        self.mastered_spells = data.get('mastered_spells', None)


### CHARACTERS
class Characters:
    def __init__(self, data) -> None:
        self.name = data['name']
        self.role = data['role']
        self.appearance = data['appearance']
        self.background = data['background']
        self.personality = data['personality']
        self.unique_skills = []

    def load_characters(self):
        with open('json_files/characters.json', 'r') as file:
            load_char_file = json.load(file)
        characters = {char: Characters(bio) for char, bio in load_char_file.items()}
        return characters



####### TODO
### GAME_FLOW ###
class GameFlow:
    def __init__(self, state) -> None:
        self.window_status = True
        # self.player = player_obj
        # character = Characters()
        self.player_state = state

    def check_input(self, p_input, flag=str):
        p_input = p_input.lower()
        chck = [int(digit) for digit in flag.split('-')]

        if p_input.lower() == 'exit':
            self.window_status = False
            return self.window_status
        
        elif self.player_state == chck:

            while p_input not in ['yes', 'y', 'exit']:
                typewritter("Please type either 'Yes' to continue or 'Exit' to exit the game. \n")
                p_input = input('> ').lower()

            if p_input in ['yes', 'y']:
                self.window_status = True
                checker = 'correct'
                return self.window_status, checker
            elif p_input == 'exit':
                self.window_status = False
                return self.window_status

    def player_input(self, at=str):
        player_input = self.check_input(input('> '), flag=at)
        return player_input


class Level():
    def __init__(self, player_obj, level_digit, input_validator):
        self.player = player_obj
        self.check = input_validator
        self.text = self.load_level_text(level_digit)

    def load_level_text(self, level):
        level_path = f'json_files/level_{level}.json'

        with open(level_path, 'r') as file:
            level_text = json.load(file)

        return level_text

### TEST GAMEFLOW
def game_flow():
    player = Player()
    game = GameFlow(player.state)
    while game.window_status:
        print("Would you like to start the game? (type 'Yes' to continue or 'Exit' to exit the game)\n")
        game.window_status = game.player_input(at='0-0-0')
        if game.window_status == False:
            continue
        print("Starting the game.")
        player.update_player(what='+lvl')
        player.update_player(what='+chp')
        player.update_player(what='+chck')

        from levels.level_1 import level_one
        level_one(Level(player_obj=player, level_digit=1, input_validator=game.check_input))

    else:
        print("Exiting the game.")

game_flow()



# class Texts():
#     def __init__(self) -> None:
#         self.console = Console()

#     def load_level_text(self, level):
#         level_path = f'json_files/level_{level}.json'

#         with open(level_path, 'r') as file:
#             level_text = json.load(file)

#         return level_text
    
#     def text_style(self, tag):

#         if 'Lenny' in tag :
#             style = "bold green3"
#         elif 'Story' in tag:
#             style = "italic grey50"
        
#         return style
        
#     def typewritter(self, text, flag='',delay=0.05):
#         try:
#             if flag == 'level':
#                 for line, values in text.items():
                    
#                     typing_index = 0
#                     while typing_index < len(values):
#                         match_pause = re.match(r'\{pause:(\d+(\.\d+)?)\}', values[typing_index:])
#                         if match_pause:
#                             pause_duration = float(match_pause.group(1))
#                             time.sleep(pause_duration)
#                             typing_index += match_pause.end()
#                         else:
#                             self.console.print(values[typing_index], end='', style=self.text_style(line))
#                             sys.stdout.flush()
#                             time.sleep(delay)
#                             typing_index += 1
#                 return True
#             else:
#                 for char in text:
#                     sys.stdout.write(char)
#                     sys.stdout.flush()
#                     time.sleep(delay)
#         except Exception as e:
#             print(f'Error occured while trying typewritter effect: {e}')
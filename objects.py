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
        player_data = self.load_player()
        self.current_level = player_data['current_level']
        self.current_chapter = player_data['current_chapter']
        self.current_checkpoint = player_data['current_checkpoint']

        self.completed_levels = []
        self.completed_chapters = []
        self.completed_check_points = []

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
    
    def update_player(self, data):
        player_data = {
            "current_level": self.current_level,
            "current_chapter": self.current_chapter,
            "current_checkpoint": self.current_checkpoint,
            "completed_levels": self.completed_levels,
            "completed_chapters": self.completed_chapters,
            "completed_check_points": self.completed_check_points,
            "hp": self.hp,
            "mp": self.mp,
            "name": self.name,
            "mastered_spells": self.mastered_spells
        }

        for k,v in player_data.items():
            for i,j in data.items():
                if k == i:
                    player_data.update({k:j})

        self._save_to_file(player_data)

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
### Modify level_1 stage to incorporate it into new design of game_flow.
### Add new checkers in check_input for the other checkpoints in the level_1.

### GAME_FLOW ###
class GameFlow:
    def __init__(self) -> None:
        self.game_status = True
        self.player = Player()
        # character = Characters()
        self.game_state = {"level": self.player.current_level, "chapter": self.player.current_chapter, "checkpoint": self.player.current_checkpoint}

    def check_input(self, input):
        input = input.lower()
        if input.lower() == 'exit':
            typewritter('Exiting the game. \n')
            self.game_status = False
            return self.game_status
        elif self.game_state == {"level": 0, "chapter": 0, "checkpoint": 0}:
            if input not in ['yes', 'y', 'exit']:
                typewritter("Please type either 'Yes' or 'y' to continue or 'Exit' to exit the game. \n")
                self.player_input()

            if input in ['yes', 'y']:
                typewritter('Starting the game... \n')
                self.player.current_level += 1
                self.player.current_chapter += 1
                self.player.current_checkpoint += 1
                self.player.update_player({"current_level": self.player.current_level, "current_chapter": self.player.current_chapter, "current_checkpoint": self.player.current_checkpoint})
                return self.game_status
            elif input == 'exit':
                self.game_status = False
                return self.game_status
        else:
            return True, input

    def player_input(self):
        player_input = self.check_input(input('> '))
        return player_input
    
    def game_flow(self):
        while self.game_status:
            print('Should we start the game?')
            self.player_input()
            time.sleep(2)
            level_one(self.game_status, self.player)

### TEST GAMEFLOW
game = GameFlow()
game.game_flow()



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
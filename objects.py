import json
from functions import typewritter

### PLAYER ###
class Player:
    def __init__(self) -> None:
        self.current_level = 0
        self.current_chapter = 0
        self.current_checkpoint = 0

        self.completed_levels = []
        self.completed_chapters = []

        self.hp = 100
        self.mp = 0
        self.name = ''
        self.mastered_spells = []

        self.state = {
            'current_level': 0,
            'current_chapter': 0,
            'current_checkpoint': 0,
            'completed_levels': [],
            'completed_chapters': [],
            'hp': 100,
            'mp': 0,
            'name': '',
            'mastered_spells': []
        }

        self.player_data = self.load_player()


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
            "current_level": self.state['current_level'],
            "current_chapter": self.state['current_chapter'],
            "current_checkpoint": self.state['current_checkpoint'],
            "completed_levels": self.state['completed_levels'],
            "completed_chapters": self.state['completed_chapters'],
            "hp": self.state['hp'],
            "mp": self.state['mp'],
            "name": self.state['name'],
            "mastered_spells": self.state['mastered_spells']
        }
        self._save_to_file(player_data)
    
    def update_player_state(self, what=''):
        if what != '':
            if what == '+lvl':
                self.state['current_level'] += 1
            elif what == '-lvl':
                self.state['current_level'] -= 1
            elif what == '+chp':
                self.state['current_chapter'] += 1
            elif what == '-chp':
                self.state['current_chapter'] -= 1
            elif what == '+chck':
                self.state['current_checkpoint'] += 1
            elif what == '-chck':
                self.state['current_checkpoint'] += 1
            
        return self.state
    
    def refresh_player_state(self):
        return self.state
    
    def save_player(self):
        self._save_to_file(self.state)

    def _save_to_file(self, data):
        try:
            with open('json_files/player_data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving player data: {e}")

    def _load_from_dict(self, data):
        self.state['current_level'] = data.get('current_level', None)
        self.state['current_chapter'] = data.get('current_chapter', None)
        self.state['current_checkpoint'] = data.get('current_checkpoint', None)

        self.state['completed_levels'] = data.get('completed_levels', None)
        self.state['completed_chapters'] = data.get('completed_chapters', None)

        self.state['hp'] = data.get('hp', None)
        self.state['mp'] = data.get('mp', None)
        self.state['name'] = data.get('name', None)
        self.state['mastered_spells'] = data.get('mastered_spells', None)


### CHARACTERS ###
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

### GAME_FLOW ###
class GameFlow:
    def __init__(self, player) -> None:
        self.window_status = True
        self.player = player
        self.player.refresh_player_state()
        self.simplified_state = [self.player.state['current_level'], self.player.state['current_chapter'], self.player.state['current_checkpoint']]

    def check_input(self, p_input):
        p_input = p_input.lower()

        if p_input.lower() == 'exit':
            self.window_status = False
            return False
        
        elif self.simplified_state == [0,0,0]:

            while p_input not in ['yes', 'y', 'exit']:
                typewritter("Please type either 'Yes' to continue or 'Exit' to exit the game. \n")
                p_input = input('> ').lower()

            if p_input in ['yes', 'y']:
                checker = 'correct'
                return True, checker
            elif p_input == 'exit':
                self.window_status = False
                return False
        elif self.simplified_state == [1,1,2]:
            return True
        elif self.simplified_state == [1,1,4]:
            typewritter("this is 1, 1, 4")
        else:
            return True

        
    def player_input(self):
        player_input = self.check_input(input('> '))
        return player_input


class Level():
    def __init__(self, level_digit, player, game_flow):
        self.player = player
        self.game_flow = game_flow
        self.text = self.load_level_text(level_digit)

    def load_level_text(self, level):
        level_path = f'json_files/level_{level}.json'

        with open(level_path, 'r') as file:
            level_text = json.load(file)

        return level_text


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
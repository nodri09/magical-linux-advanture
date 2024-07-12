import json
from functions import print_tf

class Player:
    def __init__(self) -> None:
        self.current_level = 1
        self.current_chapter = 1
        self.current_check_point = 1

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
            print_tf(f"Error loading player data: {e}", delay=0.01)
            player_data = self.create_player()
            print_tf(f"Player created", delay=0.01)
        return player_data

    def create_player(self):
        player_data = {
            "current_level": self.current_level,
            "current_chapter": self.current_chapter,
            "current_check_point": self.current_check_point,
            "completed_levels": self.completed_levels,
            "completed_chapters": self.completed_chapters,
            "completed_check_points": self.completed_check_points,
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
            "current_check_point": self.current_check_point,
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
        self.current_level = data.get('current_level', self.current_level)
        self.current_chapter = data.get('current_chapter', self.current_chapter)
        self.current_check_point = data.get('current_check_point', self.current_check_point)

        self.completed_levels = data.get('completed_levels', self.completed_levels)
        self.completed_chapters = data.get('completed_chapters', self.completed_chapters)
        self.completed_check_points = data.get('completed_check_points', self.completed_check_points)

        self.hp = data.get('hp', self.hp)
        self.mp = data.get('mp', self.mp)
        self.name = data.get('name', self.name)
        self.mastered_spells = data.get('mastered_spells', self.mastered_spells)
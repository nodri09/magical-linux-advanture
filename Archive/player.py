import json

class Player:
    def __init__(self):
        self.current_chapter = 1
        self.completed_chapters = []
        self.current_stage = 1
        self.completed_stages = []
        self.current_chp = 1
        self.completed_chps = []
        self.player_name = ""
        self.points = 0

    def create_player(self):
        player_data = {
            "name": self.player_name,
            "points": self.points,
            "current_chapter": self.current_chapter,
            "current_stage": self.current_stage,
            "current_chp": self.current_chp,
            "completed_chapters": self.completed_chapters,
            "completed_stages": self.completed_stages,
            "completed_chps": self.completed_chps
        }
        self._save_to_file(player_data)
        return player_data
    
    def modify_player(self, new_chapter, new_stage, new_chp, completed_chapters, completed_stages, completed_chps, name="Guest", new_points=0):
        self.player_name = name
        self.points += new_points
        self.current_chapter = new_chapter
        self.current_stage = new_stage
        self.current_chp = new_chp
        self.completed_chapters.extend(completed_chapters)
        self.completed_stages.extend(completed_stages)
        self.completed_chps.extend(completed_chps)
        
        player_data = {
            "name": self.player_name,
            "points": self.points,
            "current_chapter": self.current_chapter,
            "current_stage": self.current_stage,
            "current_chp": self.current_chp,
            "completed_chapters": self.completed_chapters,
            "completed_stages": self.completed_stages,
            "completed_chps": self.completed_chps
        }
        
        self._save_to_file(player_data)
        return player_data

    def _save_to_file(self, player_data):
        try:
            with open('player_data.json', 'w') as file:
                json.dump(player_data, file, indent=4)
            # print("Player data saved successfully.")
        except IOError as e:
            print(f"Error saving player data: {e}")

    def load_from_file(self):
        try:
            with open('player_data.json', 'r') as file:
                player_data = json.load(file)
            self._load_from_dict(player_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading player data: {e}")
            player_data = self.create_player()
        return player_data

    def _load_from_dict(self, player_data):
        self.player_name = player_data.get("name", self.player_name)
        self.points = player_data.get("points", self.points)
        self.current_chapter = player_data.get("current_chapter", self.current_chapter)
        self.current_stage = player_data.get("current_stage", self.current_stage)
        self.current_chp = player_data.get("current_chp", self.current_chp)
        self.completed_chapters = player_data.get("completed_chapters", self.completed_chapters)
        self.completed_stages = player_data.get("completed_stages", self.completed_stages)
        self.completed_chps = player_data.get("completed_chps", self.completed_chps)

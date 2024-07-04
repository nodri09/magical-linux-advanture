# import json

class Characters:
    def __init__(self, data) -> None:
        self.name = data['name']
        self.role = data['role']
        self.appearance = data['appearance']
        self.background = data['background']
        self.personality = data['personality']
        self.unique_skills = []

    # def load_characters(self):
    #     try:
    #         with open('json_files/characters.json', 'r') as file:
    #             characters = json.load(file)
    #         self._load_from_dict(characters)
    #     except (FileNotFoundError, json.JSONDecodeError) as e:
    #         print(f"Error loading characters: {e}")
    #     return characters

    # def _load_from_dict(self, data):
    #     self.name = data.get("name", self.name)
    #     self.role = data.get("role", self.role)
    #     self.appearance = data.get("appearance", self.appearance)
    #     self.background = data.get("background", self.background)
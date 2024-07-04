from player import Player
import json

class GameLogic:
    def __init__(self):
        self.player = Player()
        self.command_keywords = ['ls', 'cd', 'mkdir', 'touch', 'cat', 'rm', 'help']

    def handle_command(self, command):
        parts = command.split()
        if not parts:
            return "No command entered."
        
        cmd = parts[0]
        if cmd == 'help':
            return "Available commands: ls, cd, mkdir, touch, cat, rm, etc."
        elif cmd in self.command_keywords:
            # Add more detailed command handling here
            if cmd == 'ls':
                return "Directory listing..."
            elif cmd == 'cd':
                return "Changed directory to ..."
            elif cmd == 'mkdir':
                return "Directory created."
            elif cmd == 'touch':
                return "File created."
            elif cmd == 'cat':
                return "Displaying file content."
            elif cmd == 'rm':
                return "File removed."
            else:
                return f"Executed command: {cmd}"
        else:
            return "Command not recognized."

    def load_game(self):
        try:
            with open('player_data.json', 'r') as file:
                player_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            player_data = self.player.create_player()
        return player_data

    def player_status(self, data):
        status = {
            'chapter': f'chapter {data["current_chapter"]}',
            'stage': f'stage {data["current_stage"]}',
            'chp': f'checkpoint {data["current_chp"]}'
        }
        return status
    
    def save_game(self, chapter, stage, chp, points):
        self.player.modify_player(new_chapter=chapter, new_stage=stage, new_chp=chp, completed_chapters=[], completed_stages=[], completed_chps=[], new_points=points)
        # print("Game saved successfully.")
        return True

    def input_checker(self, player_status, player_input):
        if player_input.lower() == 'exit':
            return 'exit'
        # Add additional input checks as needed
        return player_status

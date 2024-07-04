# from player import Player

# player = Player()

# player.load_player()

# print(player)

# from characters import Characters

# character = Characters()

# character.load_characters()

# print(character.name)

import json
from characters import Characters
with open('json_files/characters.json', 'r') as file:
    load_characters = json.load(file)

# for char, bio in load_characters.items():
#     print(char)

characters = {char: Characters(bio) for char, bio in load_characters.items()}

print(characters['Lenny'].name)



### TODO ###
# 
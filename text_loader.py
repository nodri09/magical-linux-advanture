import json

def load_texts(filename='texts.json'):
    with open(filename, 'r') as file:
        return json.load(file)
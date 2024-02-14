import json

from synthify.character import Character
from typing import List, Union


def read_from_json(path: str) -> 'World':
        with open(path, 'r') as f:
            world_description = json.load(f)
        
        return World(world_description["name"], [Character(character) for character in world_description["characters"]], world_description["world_context"])


class World():

    def __init__(self, name: str, world_context: str, characters: List[Character] = None) -> None:
        self.name = name
        self.world_context = world_context
        if characters:
            self.characters = characters
        else:
            self.characters = []
    
    def __str__(self) -> str:
        return f"World({self.name}, {self.characters}, {self.world_context})"

    def as_dict(self) -> dict:
        return {"name": self.name, "world_context": self.world_context, "characters": [character.as_dict() for character in self.characters]}
    
    def save_as_json(self, path: str) -> None:
        with open(path, 'w') as outfile:
            json.dump(self.as_dict(), outfile)

    def add_characters(self, characters: Union[Character, List[Character]]) -> None:
        if isinstance(characters, Character):
            self.characters.append(characters)
        else:
            self.characters.extend(characters)

    def remove_characters(self, characters: Union[Character, List[Character]]) -> None:
        if isinstance(characters, Character):
            self.characters.remove(characters)
        else:
            for c in characters:
                self.characters.remove(c)
    
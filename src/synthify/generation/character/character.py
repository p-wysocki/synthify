import json

from pathlib import Path
from typing import Union, List


class Character():
    
    def __init__(self, character_description: dict) -> None:
        self.character_description = character_description

    def __str__(self) -> str:
        return f"Character({self.character_description})"
    
    def as_dict(self) -> dict:
        return self.character_description
    
    def save_as_json(self, path: Union[Path, str]) -> None:
        with open(path, 'w') as outfile:
            json.dump(self.character_description, outfile)


class CharacterFactory():
    
    def from_json(self, path: Union[Path, str]) -> List['Character']:
        with open(path, 'r') as f:
            character_description = json.load(f)
                
        character_attributes = list(character_description.keys())
        if character_attributes[0] != "characters" or len(character_attributes) != 1:
            raise ValueError("Invalid JSON file. Must start with a single 'characters' key.")

        return [Character(single_character_description) for single_character_description in character_description["characters"]]

    def generate_characters(self, character_attributes: List[str], backend: str) -> List['Character']:
        #TODO: Implement this
        if backend == "openai":
            pass
        else:
            raise ValueError(f"Invalid backend: {backend}.")

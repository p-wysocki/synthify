from synthify.generation.character import Character, CharacterFactory

import synthify
import json


def test_character_factory_from_json():
    character_factory = CharacterFactory()
    characters = character_factory.from_json("test_data/characters.json")
    assert isinstance(characters, list)
    assert isinstance(characters[0], Character)
    assert len(characters) == 2


def test_basic():
    with open("test_data/world_context.txt", "r") as f:
        world_context = f.read()

    with open('test_data/characters.json', 'r') as myfile:
        data = myfile.read()
    characters = json.loads(data)

    dreamer = synthify.Dreamer(world_context, characters)

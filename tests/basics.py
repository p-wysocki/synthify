import synthify
import json


def test_basic():
    with open("test_data/world_context.txt", "r") as f:
        world_context = f.read()

    with open('test_data/characters.json', 'r') as myfile:
        data = myfile.read()
    characters = json.loads(data)

    dreamer = synthify.Dreamer(world_context, characters)
    print(dreamer)

# TODO: generate characters

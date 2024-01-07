
from typing import Any, List, Dict, Tuple, Union, Optional

from generation.character import Character


class Dreamer():

    def __init__(self, world_context: str, characters: List[Character], backend: str = 'gpt2'):
        self.world_context = world_context
        self.characters = characters
        self.backend = backend

    def __str__(self) -> str:
        return f"Dreamer(world_context={self.world_context}, \n\ncharacters={self.characters}, \n\nbackend={self.backend})"

    def dream(self, characters=None, generate_voicelines=True):
        pass

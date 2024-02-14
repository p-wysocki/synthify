import json

from synthify.character import Character
from synthify.world import World
from synthify.config import OPENAI_API_KEY, OPENAI_CHAT_TEMPERATURE, OPENAI_MODEL
from openai import OpenAI
from typing import List, Dict


def _get_role_prompt(character_attributes: List[str]) -> List[Dict[str, str]]:
    prompt = [
        {"role": "user",
         "content": "I need a character with the following attributes: " + ", ".join(character_attributes) + ". "},
    ]
    return prompt


def _get_system_prompt(world_context: str) -> List[Dict[str, str]]:
    return [
        {"role": "system",
         "content": "You are a creative writer, tasked with creating characters. The characters must be unique and interesting. "
         "You have a list of character attributes to help you, as well as background information about the world they live in. "
         "The characters have to be different from one another, and they have to be interesting. "
         "You are not limited to the attributes provided, you can add your own. Return a character in JSON format, "
         "with the keys being the character attributes, and the values being the character's values for those attributes. "
         f"The world context is: {world_context}. "},
    ]


def _request_chat_completion(openai_client: OpenAI, prompt: List[Dict[str, str]], debug: bool=False) -> str:
    if debug:  # do not waste API calls in debug mode
        completion = {"choices": [{"text": "This is a mock response."}]}
    else:
        completion = openai_client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=prompt,
        temperature=OPENAI_CHAT_TEMPERATURE,
        )

    return completion.choices[0].message.content


def generate_characters(world: World, character_attributes: List[str], characters_to_generate: int = 1) -> List[Dict[str, str]]:
    # TODO: Make model remember last few characters to avoid duplication?
    # TODO: How to make sure the characters are interesting?
    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    if len(world.characters) < 1:
        raise ValueError(f"Must generate at least one character. World {world.name} has {len(world.characters)} characters.")
    prompt = _get_system_prompt(world.world_context) + _get_role_prompt(character_attributes)
    generated_characters = []
    for _ in range(characters_to_generate):
        character = _request_chat_completion(openai_client, prompt)
        try:
            generated_characters.append(Character(json.loads(character)))
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid LLM response: {character}.\nThe prompt was: {prompt}.\nError: {e}")

    return generated_characters


def generate_dialogue():
    #TODO: Implement this
    pass

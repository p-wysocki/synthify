import json

from synthify.config import OPENAI_API_KEY
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


def _get_openai_client() -> OpenAI:
    return OpenAI(api_key=OPENAI_API_KEY)


def _request_chat_completion(openai_client: OpenAI, prompt: List[Dict[str, str]], debug: bool=False) -> str:
    if debug:  # do not waste API calls in debug mode
        completion = {"choices": [{"text": "This is a mock response."}]}
    else:
        completion = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=1.7,
        )

    return completion.choices[0].message.content


def generate_characters(world_context: str, character_attributes: List[str], characters_to_generate: int = 1) -> List[Dict[str, str]]:
    # TODO: Make model remember last few characters to avoid duplication?
    # TODO: How to make sure the characters are interesting?
    openai_client = _get_openai_client()
    if characters_to_generate < 1:
        raise ValueError("Must generate at least one character.")
    prompt = _get_system_prompt(world_context) + _get_role_prompt(character_attributes)
    generated_characters = []
    for _ in range(characters_to_generate):
        generated_characters.append(json.loads(_request_chat_completion(openai_client, prompt)))

    return generated_characters

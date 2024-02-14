import synthify.generation.backends.openai_api as openai_api


def test_api_key():
    assert openai_api.OPENAI_API_KEY

def test_openai_api_access():
    assert openai_api.request_chat_completion()

def test_character_generation():
    world_context_small = "A fantasy world with dragons and magic."
    characters = openai_api.generate_characters(world_context_small, ["name", "age", "occupation"], 3)
    #TODO: How to properly validate an LLM response?
    assert len(characters) == 3

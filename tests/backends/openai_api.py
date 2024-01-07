import synthify.generation.backends.openai_api as openai_api

def test_openai_api_access():
    assert openai_api.OPENAI_API_KEY != None
    openai_api.get_response()

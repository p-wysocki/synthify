import synthify

from pathlib import Path



# OpenAI --------------------------------------------------------------------------------------------------------------------
OPENAI_API_KEY_PATH = Path(synthify.__file__) / Path("..") / Path("openai_key.txt")

try:
    with open(OPENAI_API_KEY_PATH, "r") as f:
        OPENAI_API_KEY = f.read()
except FileNotFoundError as e:
    print("Please create a file called openai_api_token.txt in the root directory and paste your OpenAI API key in it.")
    raise

# ----------------------------------------------------------------------------------------------------------------------------

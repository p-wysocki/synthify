import os

# OpenAI --------------------------------------------------------------------------------------------------------------------
OPENAI_CHAT_TEMPERATURE = 1.7
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
OPENAI_MODEL = "gpt-3.5-turbo"
if not OPENAI_API_KEY:
    raise RuntimeError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
# ----------------------------------------------------------------------------------------------------------------------------

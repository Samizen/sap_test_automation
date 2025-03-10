from dotenv import load_dotenv
from os import getenv

load_dotenv()

MODEL= "gpt-4o-mini"
ROWS_TO_SKIP_WHILE_READING_CSV=2
INPUT_FOLDER= "inputs"
OUTPUT_FOLDER= "outputs"
_API_KEY= getenv("OPENAI_API_KEY")
if not _API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def get_api_key():
    return _API_KEY
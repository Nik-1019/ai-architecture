# model_provider.py
import os
from functools import lru_cache
from dotenv import load_dotenv
from google import genai

load_dotenv()
MODEL_ID = "gemini-2.5-flash"

@lru_cache
def get_client() -> genai.Client:
    return genai.Client()

def generate(prompt: str) -> str:
    response = get_client().models.generate_content(
        model=MODEL_ID, contents=prompt
    )
    return response.text
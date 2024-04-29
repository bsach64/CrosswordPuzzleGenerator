import logging
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json


def get_words_hints(n: int) -> dict:
    load_dotenv()
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    model = genai.GenerativeModel("gemini-pro")

    logging.info("Generating words and hints...")
    prompt = f"""
    generate words and hints for a {n} word crossword puzzle.
    Response should be of the form {{\"WORD\":\"HINT\",\"WORD\":\"HINT\"}}
    Response should be in a single line.
    """
    response = model.generate_content(prompt)
    hw = json.loads(response.text)
    return {w.lower(): hw[w].lower() for w in hw}

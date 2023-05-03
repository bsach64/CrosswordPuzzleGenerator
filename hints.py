"""Generates hints for words using ChatGPT API"""

import openai

with open("api_key.txt") as file:
    file_content = file.readline()
    api_key = file_content

openai.api_key = api_key


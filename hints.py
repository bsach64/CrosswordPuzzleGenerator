"""Generates hints for words using ChatGPT API"""

import openai
import json

with open("api_key.txt") as file:
    file_content = file.readline()
    api_key = file_content

openai.api_key = api_key


with open("crossword.json") as file:
    crossword = json.load(file)

for word in crossword:
    prompt = f"generate a crossword hint for the word {word}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    raw_answer = str(response["choices"][0]["text"])
    unwanted = ['\\', '\n', '\'', '\"']
    for character in unwanted:
        raw_answer = raw_answer.replace(character,'')
    crossword[word] = raw_answer

with open("crossword.json", "w") as file:
    json.dump(crossword, file)
"""Generates n words using ChatGPT API"""

import openai
import json

while True:
    try:
        n = int(input("Number of words to generate: "))
        break
    except ValueError:
        ...

with open("api_key.txt") as file:
    file_content = file.readline()
    api_key = file_content

openai.api_key = api_key

prompt = f"suggest {n} words"

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.8,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
)

raw_answer = str(response["choices"][0]["text"])

answer = raw_answer[2:]

final_answer = ""
for character in answer:
    if character.isdigit() or character == "." or character == " ":
        ...
    else:
        final_answer = final_answer + character


with open("words.txt", "w") as file:
    file.write(final_answer)
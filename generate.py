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

for i in range(n):
    prompt = f"generate one word"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    raw_answer = str(response["choices"][0]["text"])
    print(raw_answer[2:])
    with open("words.txt", "a", newline="") as file:
        raw_answer = raw_answer.replace('\n','') 
        file.write(raw_answer + '\n')

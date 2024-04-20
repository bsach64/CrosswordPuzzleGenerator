"""Generates n words using ChatGPT API"""

import openai
import json

def generate_words(n):
    print("Generating Words...")
    with open("api_key.txt") as file:
        file_content = file.readline()
        api_key = file_content

    openai.api_key = api_key

    prompt = f"generate {n} words for a crossword puzzle."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    raw_answer = str(response["choices"][0]["text"]).replace('\n', '').replace('\n', '')
    numbers = [str(i) for i in range(10)]
    for number in numbers:
        if number in raw_answer:
            raw_answer = raw_answer.replace(number, '')
    words = raw_answer.strip().split(" ")

    crossword = {word.lower():"" for word in words}

    with open("crossword.json", "w") as file:
        json.dump(crossword, file)

def generate_hints():
    with open("api_key.txt") as file:
        file_content = file.readline()
        api_key = file_content

    openai.api_key = api_key
    print("Generating Hints...")

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

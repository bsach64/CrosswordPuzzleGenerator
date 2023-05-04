"""Generates n words using ChatGPT API"""

import openai
import json


def main():
    generate_words()
    generate_hints()

def generate_words():
    while True:
        try:
            n = int(input("Number of words to generate: "))
            break
        except ValueError:
            ...
    print("Generating Words...")
    with open("api_key.txt") as file:
        file_content = file.readline()
        api_key = file_content

    openai.api_key = api_key

    words = {}

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
        raw_answer = raw_answer.replace('\n','')
        words[raw_answer] = ""

    with open("crossword.json", "w") as file:
        json.dump(words, file)


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

if __name__ == "__main__":
    main()
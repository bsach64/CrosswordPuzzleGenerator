import json

def input_words(words: list[str]):
    crossword: dict = {word:"" for word in words}
    with open("crossword.json", "w") as file:
        json.dump(crossword, file)

def get_words(filename: str) -> list[str]:
    crossword: dict = {}
    with open(filename) as file:
        crossword = json.load(file)
    return list(crossword.keys())

import json

words = []

with open("crossword.json") as file: 
    crossword = {}
    crossword = json.load(file)
    for word in crossword:
        words.append(word)


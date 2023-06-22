import json

def input_words(words):
    crossword = {}

    for word in words:
        crossword[word] = ""

    with open("crossword.json", "w") as file:
        json.dump(crossword, file)

def get_words(filename):
    words = []
    with open(filename) as file:
        crossword = {}
        crossword = json.load(file)
        for word in crossword:
            words.append(word)  
    return words
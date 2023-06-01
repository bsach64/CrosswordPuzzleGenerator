import json

def input_words():
    words = input("Enter the list of words separated by spaces: ")
    words = words.split(" ")

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
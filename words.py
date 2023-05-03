import json


def input_words():
    words = input("Enter the list of words separated by spaces: ")
    words = words.split(" ")

    crossword = {}

    for word in words:
        crossword[word] = ""

    with open("crossword.json", "w") as file:
        json.dump(words, file)
import json
from generate import *
from words import input_words, get_words
from best import best_board
from generate_image import *

def maker(number):
    print("Generating Words...")
    generate_words(number)
    print("Generating Hints...")
    generate_hints()
    print("Generating Crossword...")
    words = get_words("crossword.json")
    crossword = best_board(words, 500)
    for line in crossword.board:
        print(line)
    empty_crossword(crossword)
    filled_crossword(crossword)
    solve = []
    with open("crossword.json") as file:
        hints = {}
        hints = json.load(file)
    solve.append("ACROSS")
    for word in crossword.info:
        if crossword.info[word].direction == "h":
            solve.append(str(crossword.info[word].order) + ". " + hints[word])
    solve.append("DOWN")
    for word in crossword.info:
        if crossword.info[word].direction == "v":
            solve.append(str(crossword.info[word].order) + ". " + hints[word])
    return solve

def make_from_words(words):
    words = words.split(" ")
    input_words(words)
    print("Generating Hints...")
    generate_hints()
    print("Generating Crossword...")
    words = get_words("crossword.json")
    crossword = best_board(words, 500)
    for line in crossword.board:
        print(line)
    empty_crossword(crossword)
    filled_crossword(crossword)
    solve = []
    with open("crossword.json") as file:
        hints = {}
        hints = json.load(file)
    solve.append("ACROSS")
    for word in crossword.info:
        if crossword.info[word].direction == "h":
            solve.append(str(crossword.info[word].order) + ". " + hints[word])
    solve.append("DOWN")
    for word in crossword.info:
        if crossword.info[word].direction == "v":
            solve.append(str(crossword.info[word].order) + ". " + hints[word])
    return solve

                

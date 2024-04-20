import json
from words_hints_req import get_words_hints
from puzzle import best_board
from crossword_image import *
import logging

def maker(number: int):
    logging.info("Generating words and hints...")
    hw: dict = get_words_hints(number)

    logging.info("Generating Crossword...")
    words: list[str] = list(hw.keys())
    crossword = best_board(words, 500)
    empty_crossword(crossword.board)
    filled_crossword(crossword.board)
    solve = []
    solve.append("ACROSS")
    for word in crossword.info:
        if crossword.info[word].direction == "h":
            solve.append(str(crossword.info[word].order) + ". " + hw[word])
    solve.append("DOWN")
    for word in crossword.info:
        if crossword.info[word].direction == "v":
            solve.append(str(crossword.info[word].order) + ". " + hw[word])
    return solve

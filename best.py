import random
from puzzle import Crossword, make
import copy


def best_board(words, iterations):
    max_score = 0
    for _ in range(iterations):
        random.shuffle(words)
        crossword = Crossword()
        crossword = make(words)
        crossword_score = crossword.score()
        if crossword_score > max_score:
            max_score = crossword_score
            result = copy.deepcopy(crossword)

    return result

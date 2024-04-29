from words_hints_req import get_words_hints
from puzzle import best_board
from crossword_image import empty_crossword, filled_crossword
import logging


def maker(number: int):
    logging.info("Generating words and hints...")
    hw: dict = get_words_hints(number)

    logging.info("Generating Crossword...")
    words: list[str] = list(hw.keys())
    crossword = best_board(words, 500)
    empty_crossword(crossword.board)
    filled_crossword(crossword.board)
    sol_across, sol_col = ["ACROSS"], ["DOWN"]
    for word in crossword.info:
        if crossword.info[word].direction == "h":
            sol_across.append(f"{crossword.info[word].order}. {hw[word]}")
        else:
            sol_col.append(f"{crossword.info[word].order}. {hw[word]}")
    return sol_across + sol_col

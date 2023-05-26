import random 
from puzzle import make
from score import score

def best_board(words, iterations):
    max_score = 0
    for _ in range(iterations):
        random.shuffle(words)
        board, placed_words = make(words)
        board_score = score(board, placed_words)
        if board_score > max_score:
            max_score = board_score
            final_words = placed_words
            result = board
    
    return result, final_words


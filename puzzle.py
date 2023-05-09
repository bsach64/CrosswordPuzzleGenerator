import json


def main():
    words = []

    with open("crossword.json") as file: 
        crossword = {}
        crossword = json.load(file)
        for word in crossword:
            words.append(word)

    board = make(words)
    print(board)

def make(words):
    board = [[None for i in range(25)] for j in range(25)]
    words = sorted(words, key=len, reverse=True)
    placed_words = []
    first_word = words[0]
    placed_words.append(first_word)
    filled_indexes = []

    start_index = 13 - (len(first_word) // 2)

    for character in first_word:
        board[13][start_index] = character
        filled_indexes.append((13, start_index))
        start_index += 1
    
    return board


def place(word, crossword, placement):
    ...

def can_place():
    ...


class Placement:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


if __name__ == "__main__":
    main()
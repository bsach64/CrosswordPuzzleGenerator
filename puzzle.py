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
    SIZE = 25
    max_words = len(words)
    board = [[None for i in range(SIZE)] for j in range(SIZE)]
    words = sorted(words, key=len, reverse=True)
    placed_words = []
    
    # Placing the first word
    first_word = words.pop(0)
    placed_words.append(first_word)
    start_index = 13 - (len(first_word) // 2)
    place(first_word, board, Placement(row=13, column=start_index, direction="h"))
    count = 1

    while count < max_words and len(words) > 0:
        current_word = words.pop(0)
        for character in current_word:
            for i in range(SIZE):
                for j in range(SIZE):
                    if character == board[i][j]:
                        location, ok = can_place()
                        if ok:
                            place()
                            count += 1


    return board


def place(word, board, placement):
    if placement.direction == "h":
        shift = 0
        for character in word:
            board[placement.row][placement.column + shift] = character
            shift += 1

    elif placement.direction == "v":
        shift = 0
        for character in word:
            board[placement.row + shift][placement.column] = character

def can_place():
    return True


class Placement:
    def __init__(self, row, column, direction):
        self.row = row
        self.column = column  
        self.direction = direction

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, direction):
        if direction not in ["h", "v"]:
            raise ValueError("Invalid Direction")
        self._direction = direction

if __name__ == "__main__":
    main()
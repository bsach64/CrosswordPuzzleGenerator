import copy
import random

SIZE = 100
MID = SIZE // 2

class Crossword:
    def __init__(self):
        self.board = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]
        self.info = dict()

    def place(self, word, placement):
        if placement.direction == "h":
            for i, ch in enumerate(word):
                self.board[placement.row][placement.column + i] = ch
        elif placement.direction == "v":
            for i, ch in enumerate(word):
                self.board[placement.row + i][placement.column] = ch
        self.info[word] = placement

    def score(self):
        rows, columns = len(self.board), len(self.board[0])
        size_ratio = rows / columns
        if rows > columns:
            size_ratio = columns / rows
        filled, empty = 0, 0
        for i in range(rows):
            for j in range(columns):
                if self.board[i][j] == ' ':
                    empty += 1
                else:
                    filled += 1
        filled_ratio = filled / empty
        return ((len(self.info) * 40) + (size_ratio * 10) + (filled_ratio * 20))

    def create_order(self):
        placed_order = 1
        all_words = list(self.info.keys())
        for word_one in all_words:
            for word_two in all_words:
                if word_one != word_two:
                    if self.info[word_one].row == self.info[word_two].row and self.info[word_one].column == self.info[word_two].column:
                        self.info[word_one].order = placed_order
                        self.info[word_two].order = placed_order
                        all_words.remove(word_one)
                        all_words.remove(word_two)
                        placed_order += 1

        for word in all_words:
            self.info[word].order = placed_order
            placed_order += 1

        for word in self.info:
            if len(self.board[self.info[word].row][self.info[word].column]) < 2:
                self.board[self.info[word].row][self.info[word].column] = str(self.info[word].order) + self.board[self.info[word].row][self.info[word].column]

    def reduce(self):
        final_board = [row for row in self.board if any(cell != ' ' for cell in row)]
        transposed_board = list(zip(*final_board))
        transposed_board = [col for col in transposed_board if any(cell != ' ' for cell in col)]
        return_board = list(zip(*transposed_board))
        return_board = [list(row) for row in return_board]
        self.board = return_board


def make(words):
    crossword, i = Crossword(), 0
    first_word = words[i]
    i += 1
    start_index = MID - (len(first_word) // 2)
    crossword.place(first_word , Placement(row=MID, column=start_index, direction="h"))

    while i < len(words):
        current_word = words[i]
        i += 1
        for letter in current_word:
            for j in range(SIZE):
                for k in range(SIZE):
                    if letter == crossword.board[j][k]:
                        location, ok = can_place(current_word, crossword.board, j, k)
                        if ok:
                            if current_word not in crossword.info:
                                crossword.place(current_word, location)

    crossword.create_order()
    crossword.reduce()
    return crossword

class Placement:
    def __init__(self, row, column, direction, order=0):
        self.row = row
        self.column = column  
        self.direction = direction
        self.order = order

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction not in ["h", "v"]:
            raise ValueError("Invalid Direction")
        self._direction = direction


def can_place(current_word, board, row, column):
    position = current_word.find(board[row][column])
    flag_vertical, flag_horizontal = True, True
    if position == -1:
        return None, False
    first_half, second_half = current_word[:position], current_word[(position + 1):]
    for i in range(1, (len(first_half) + 2)):
        for j in range(-1, 2):
            if row - i < 0 or column + j < 0 or \
                column + j >= len(board[row - i]) or board[row - i][column + j] != ' ':
                flag_vertical = False
                break

    for i in range(1, (len(second_half) + 2)):
        for j in range(-1, 2):
            if row + i >= len(board) or column + j < 0 or \
                column + j >= len(board) or board[row + i][column + j] != ' ':
                flag_vertical = False

    if flag_vertical:
        return Placement(row=(row - len(first_half)), column=column, direction="v"), True

    for j in range(1, (len(first_half) + 2)):
        for i in range(-1, 2):
            if row + i < 0 or row + i >= len(board) or \
               column - j < 0 or board[row + i][column - j] != ' ':
                flag_horizontal = False

    for j in range(1, (len(second_half) + 2)):
        for i in range(-1, 2):
            if row + i < 0 or row + i >= len(board) or \
                column + j >= len(board) or board[row + i][column + j] != ' ':
                flag_horizontal = False

    if flag_horizontal:
        return Placement(row=row, column=(column - len(first_half)), direction="h"), True
    return None, False


def best_board(words, iterations):
    max_score, result = 0, None
    for _ in range(iterations):
        random.shuffle(words)
        crossword = Crossword()
        crossword = make(words)
        crossword_score = crossword.score()
        if crossword_score > max_score:
            max_score = crossword_score
            result = copy.deepcopy(crossword)

    return result

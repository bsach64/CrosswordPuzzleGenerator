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
            shift = 0
            for character in word:
                self.board[placement.row][placement.column + shift] = character
                shift += 1
            self.info[word] = placement
        elif placement.direction == "v":
            shift = 0
            for character in word:
                self.board[placement.row + shift][placement.column] = character            
                shift += 1
            self.info[word] = placement

    def score(self):
        number_of_words = len(self.info)
        rows = len(self.board)
        columns = len(self.board[0])
        size_ratio = rows / columns
        if rows > columns:
            size_ratio = columns / rows
        filled = 0
        empty = 0
        for i in range(rows):
            for j in range(columns):
                if self.board[i][j] == ' ':
                    empty += 1
                else:
                    filled += 1
        filled_ratio = filled / empty
        return ((number_of_words * 40) + (size_ratio * 10) + (filled_ratio * 20))

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

    def append_order(self):
        for word in self.info:
            if len(self.board[self.info[word].row][self.info[word].column]) < 2:
                self.board[self.info[word].row][self.info[word].column] = str(self.info[word].order) + self.board[self.info[word].row][self.info[word].column]

    def reduce(self):
        final_board = copy.deepcopy(self.board)
        final_board = [row for row in final_board if any(cell != ' ' for cell in row)]
        transposed_board = list(zip(*final_board))
        transposed_board = [col for col in transposed_board if any(cell != ' ' for cell in col)]
        return_board = list(zip(*transposed_board))
        return_board = [list(row) for row in return_board]
        self.board = return_board

def make(words):
    max_words = len(words)
    crossword = Crossword()
    word_list = copy.deepcopy(words)
    first_word = word_list.pop(0)
    start_index = MID - (len(first_word) // 2)
    crossword.place(first_word , Placement(row=MID, column=start_index, direction="h"))
    count = 1

    while count < max_words and len(word_list) > 0:
        current_word = word_list.pop(0)
        for letter in current_word:
            for j in range(SIZE):
                for k in range(SIZE):
                    if letter == crossword.board[j][k]:
                        location, ok = can_place(current_word, crossword.board, j, k)
                        if ok:
                            if current_word not in crossword.info:
                                crossword.place(current_word, location)
                                count += 1
    
    crossword.create_order()
    crossword.append_order()
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
    flag_vertical = 1
    flag_horizontal = 1
    if position != -1:
        first_half = current_word[:position]
        second_half = current_word[(position + 1):]
        for i in range(1, (len(first_half) + 2)):
            for j in range(-1, 2):               
                try:
                    if board[row - i][column + j] == ' ':
                        flag_vertical *= 1
                    else:
                        flag_vertical = 0
                        break
                except IndexError:
                    flag_vertical = 0
        for i in range(1, (len(second_half) + 2)):
            for j in range(-1, 2):
                try:
                    if board[row + i][column + j] == ' ':
                        flag_vertical *= 1
                    else:
                        flag_vertical = 0
                        break
                except IndexError:
                    flag_vertical = 0
        if flag_vertical == 1:
            return [Placement(row=(row - len(first_half)), column=column, direction="v"), True]

        for j in range(1, (len(first_half) + 2)):
            for i in range(-1, 2):
                try:
                    if board[row + i][column - j] == ' ':
                        flag_horizontal *= 1
                    else:
                        flag_horizontal = 0
                        break
                except IndexError:
                    flag_horizontal = 0
        for j in range(1, (len(second_half) + 2)):
            for i in range(-1, 2):
                try:
                    if board[row + i][column + j] == ' ':
                        flag_horizontal *= 1
                    else:
                        flag_horizontal = 0
                        break
                except IndexError:
                    flag_horizontal = 0

        if flag_horizontal == 1:
            return [Placement(row=row, column=(column - len(first_half)), direction="h"), True]
    else:
        return [None, False]
    return [None, False]


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

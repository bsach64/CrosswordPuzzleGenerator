import copy

SIZE = 100
MID = SIZE // 2

def make(words):
    max_words = len(words)
    board = [[' ' for i in range(SIZE)] for j in range(SIZE)]
    placed_words = []
    word_list = copy.deepcopy(words)
    # Placing the first word
    first_word = word_list.pop(0)
    start_index = 13 - (len(first_word) // 2)
    place(first_word , board, Placement(row=13, column=start_index, direction="h"))
    count = 1

    while count < max_words and len(word_list) > 0:
        current_word = word_list.pop(0)
        temp = find(current_word, board)
        if temp != None:
            placed_words.append(current_word)
            board = temp

    board = reduce(board)
    
    return board, placed_words


def find(word, board):
    for letter in word[1:len(word)-1]:
        for j in range(SIZE):
            for k in range(SIZE):
                if letter == board[j][k]:
                    location, ok = can_place(word, board, j, k)
                    if ok:
                        return place(word, board, location)

def place(word, board, placement):
    if placement.direction == "h":
        shift = 0
        for character in word:
            board[placement.row][placement.column + shift] = character
            shift += 1
        return board
    elif placement.direction == "v":
        shift = 0
        try:
            for character in word:
                board[placement.row + shift][placement.column] = character            
                shift += 1
            return board
        except IndexError:
            return None
    else:
        return None
        
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


def reduce(board):
    empty_rows = []
    for i in range(SIZE):
        empty_row = 1
        for j in range(SIZE):
            if board[i][j] == ' ':
                empty_row *= 1
            else:
                empty_row = 0
                break
        if empty_row == 1:
            empty_rows.append(i)
            
    filled_rows = []
    for i in range(SIZE):
        if i not in empty_rows:
            filled_rows.append(board[i])
    
    cols = []
    for i in range(SIZE):
        temp = 1
        for j in range(len(filled_rows)):
            if filled_rows[j][i] == ' ':
                temp *= 1
            else:
                temp = 0
                break
        if temp == 1:
            cols.append(i)

    final = []
    for row in filled_rows:
        temp = []
        for j in range(len(row)):
            if j not in cols:
                temp.append(row[j])
        final.append(temp)

    return final


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

def score(board, placed_words):
    number_of_words = len(placed_words)
    rows = len(board)
    columns = len(board[0])
    size_ratio = rows / columns
    if rows > columns:
        size_ratio = columns / rows
    filled = 0
    empty = 0
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == ' ':
                empty += 1
            else:
                filled += 1
    filled_ratio = filled / empty
    return ((number_of_words * 40) + (size_ratio * 10) + (filled_ratio * 20))


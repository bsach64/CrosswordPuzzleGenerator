import json


SIZE = 30
MID = SIZE // 2

def main():
    words = []

    with open("crossword.json") as file: 
        crossword = {}
        crossword = json.load(file)
        for word in crossword:
            words.append(word)

    board = make(words)
    for line in board:
        print(line)

def make(words):
    max_words = len(words)
    board = [[None for i in range(SIZE)] for j in range(SIZE)]
    words = sorted(words, key=len, reverse=True)
    
    # Placing the first word
    first_word = words.pop(0)
    start_index = 13 - (len(first_word) // 2)
    place(first_word, board, Placement(row=13, column=start_index, direction="h"))
    count = 1

    while count < max_words and len(words) > 0:
        current_word = words.pop(0)
        temp = find(current_word, board)
        if temp != None:
            board = temp

    return board


def find(word, board):
    for letter in word:
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
        for character in word:
            board[placement.row + shift][placement.column] = character            
            shift += 1
        return board
    else:
        return None
        
def can_place(current_word, board, row, column):
    flag_row_first = 1
    flag_row_two = 1
    flag_column_first = 1
    flag_column_two = 1
    position = current_word.find(board[row][column])
    if position != -1:
        first_half = current_word[:position]
        second_half = current_word[position:]
        for i in range(1, len(first_half) + 1):
            if board[row - i][column] == None:
                flag_row_first *= 1
            else:
                flag_row_first = 0
                break 
        for i in range(1, len(second_half) + 1):
            if board[row + i][column] == None:
                flag_row_two *= 1
            else:
                flag_row_two = 0
                break
        if flag_row_first == 1 and flag_row_two == 1:
            return [Placement(row=(row - len(first_half)), column=column, direction="v"), True]

        for i in range(1, len(first_half) + 1):
            if board[row][column - i] == None:
                flag_column_first *= 1
            else:
                flag_column_two = 0
                break
        for i in range(1, len(second_half) + 1):
            if board[row][column + i] == None:
                flag_column_first *= 1
            else:
                flag_column_two = 0
                break 
        if flag_column_first == 1 and flag_column_two == 1:
            return [Placement(row=row, column=(column- len(first_half)), direction="h"), True]
    else:
        return [None, False]
    return [None, False]

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
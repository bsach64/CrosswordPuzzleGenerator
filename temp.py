SIZE = 40
MID = SIZE // 2

def main():
    '''board = [[None for i in range(SIZE)] for j in range(SIZE)]
    place("one", board, Placement(row=13, column=(13 - (len("one") // 2)), direction="h"))
    location, ok = can_place("two", board, 13, 12)
    if ok:
        print(location.row, location.column, location.direction)
        board = place("two", board, location)
        print(board[11][12])
        l, o = can_place("three", board, 11, 12)
        if o:
            board = place("three", board, l)
        f, ow = can_place("there", board, 11, 15)
        if ow:
            board = place("there", board, f)
        for i in board:
            print(i)

    else:
        print("Not")'''

    cross = [[None for i in range(SIZE)] for j in range(SIZE)]
    words = ["feline", "joyous","scrub", "exodus", "pecan", "stereo","ravine", "jester", "whisky", "squab", "algae","jungle","garble", "jubilee"]
    cross = place(words[0], cross, Placement(row=MID, column=(MID - (len(words[0]) // 2)), direction="h"))
    for i in range(1, (len(words))):
        temp = find(words[i], cross)
        if temp != None:
            cross = temp
        else:
            print("no")

    for line in cross:
        print(line)


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
    flag_row = 1
    flag_column = 1
    position = current_word.find(board[row][column])
    if position != -1:
        first_half = current_word[:position]
        second_half = current_word[position:]
        for i in range(1, len(first_half) + 1):
            if board[row - i][column] == None:
                flag_row *= 1
            else:
                flag_row = 0
                break 
        for i in range(1, len(second_half) + 1):
            if board[row + i][column] == None:
                flag_row *= 1
            else:
                flag_row = 0
                break
        if flag_row == 1:
            return [Placement(row=(row - len(first_half)), column=column, direction="v"), True]

        for i in range(1, len(first_half) + 1):
            if board[row][column - i] == None:
                flag_column *= 1
            else:
                flag_column = 0
                break
        for i in range(1, len(second_half) + 1):
            if board[row][column + i] == None:
                flag_column *= 1
            else:
                flag_column = 0
                break 
        if flag_column == 1:
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

main()
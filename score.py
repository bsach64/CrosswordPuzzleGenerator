def score(placed_words, board):
    number_of_words = len(placed_words)
    rows = len(board)
    columns = len(board[0])
    size_ratio = rows / columns
    if rows > columns:
        size_ratio = columns / rows
    filled = 0
    empty = 0
    for i in rows:
        for j in columns:
            if board[i][j] == ' ':
                empty += 1
            else:
                filled += 1
    filled_ratio = filled / empty
    return ((number_of_words * 40) + (size_ratio * 10) + (filled_ratio * 20))


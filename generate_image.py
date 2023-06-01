import copy
     
def empty_crossword(board):
    """
    Save crossword assignment to an image file.
    """
    from PIL import Image, ImageDraw, ImageFont
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==' ' or board[i][j]=='0':
                board[i][j]=None
    
    letters=copy.deepcopy(board)
    img = Image.new(
        "RGBA",
        (len(board[1]) * cell_size,
            len(board) * cell_size),
        "black"
    )
    font = ImageFont.truetype(r"OpenSans-Regular.ttf",120)
    draw = ImageDraw.Draw(img)

    for i in range(len(letters)):
        for j in range(len(letters[i])):

            rect = [
                (j * cell_size + cell_border,
                    i * cell_size + cell_border),
                ((j + 1) * cell_size - cell_border,
                    (i + 1) * cell_size - cell_border)
            ]
            if letters[i][j]:
                draw.rectangle(rect, fill="white")
    img.show()
    print(img.size)
    img.save('crossword.png')

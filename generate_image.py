import copy
from puzzle import reduce
     
def empty_crossword(crossword):
    """
    Save crossword_board assignment to an image file.
    """
    from PIL import Image, ImageDraw, ImageFont
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    img = Image.new(
        "RGBA",
        (len(crossword.board[1]) * cell_size,
            len(crossword.board) * cell_size),
        "black"
    )
    font = ImageFont.truetype(r"OpenSans-Regular.ttf",65)
    draw = ImageDraw.Draw(img)
    for i in range(len(crossword.board)):
        for j in range(len(crossword.board[i])):

            rect = [
                (j * cell_size + cell_border,
                    i * cell_size + cell_border),
                ((j + 1) * cell_size - cell_border,
                    (i + 1) * cell_size - cell_border)
            ]
            if crossword.board[i][j] != ' ':
                draw.rectangle(rect, fill="white")
                for word in crossword.info:
                    if crossword.info[word].row == i and crossword.info[word].column == j:
                        w, h = draw.textsize(str(crossword.info[word].order), font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                            rect[0][1] + ((interior_size - h) / 2) - 10),
                            str(crossword.info[word].order), font = font ,fill="black"
                        )  
    img.save('crossword_board.png')


def filled_crossword(crossword):
    from PIL import Image, ImageDraw, ImageFont
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    # Create a blank canvas
    crossword_board = reduce(crossword.board)
    img = Image.new(
        "RGBA",
        (len(crossword_board[1]) * cell_size,
            len(crossword_board) * cell_size),
        "black"
    )
    font = ImageFont.truetype(r"OpenSans-Regular.ttf",65)
    draw = ImageDraw.Draw(img)

    for i in range(len(crossword_board)):
        for j in range(len(crossword_board[i])):

            rect = [
                (j * cell_size + cell_border,
                    i * cell_size + cell_border),
                ((j + 1) * cell_size - cell_border,
                    (i + 1) * cell_size - cell_border)
            ]
            if crossword_board[i][j] != ' ':
                draw.rectangle(rect, fill="white")
                if crossword_board[i][j]:
                    w, h = draw.textsize(crossword_board[i][j], font=font)
                    draw.text(
                        (rect[0][0] + ((interior_size - w) / 2),
                        rect[0][1] + ((interior_size - h) / 2) - 10),
                        crossword_board[i][j], font = font ,fill="black"
                    )
    img.show()
    print(img.size)
    img.save('filled_crossword.png')
    
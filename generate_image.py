from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont


def empty_crossword(crossword):
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    img = Image.new(
        "RGBA",
        (len(crossword.board[1]) * cell_size,
            len(crossword.board) * cell_size),
        "black"
    )
    font = ImageFont.truetype(r"OpenSans-Regular.ttf",30)
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
            if len(crossword.board[i][j]) > 1:
                w, h = draw.textsize(crossword.board[i][j][:-1], font=font)
                draw.text(
                        (rect[0][0] + (((interior_size - w) / 2) - 27),
                        rect[0][1] + ((interior_size - h) / 2) - 35),
                        crossword.board[i][j][:-1], font = font ,fill="black"
                    )
    print("image empty generated")
    img.save('./static/crossword_board.png')

def filled_crossword(crossword):
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    img = Image.new(
        "RGBA",
        (len(crossword.board[1]) * cell_size,
            len(crossword.board) * cell_size),
        "black"
    )
    font_small = ImageFont.truetype(r"OpenSans-Regular.ttf",30)
    font = ImageFont.truetype(r"OpenSans-Regular.ttf",55)
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
                if len(crossword.board[i][j]) > 1:
                    w, h = draw.textsize(crossword.board[i][j][:-1], font=font_small)
                    draw.text(
                            (rect[0][0] + (((interior_size - w) / 2) - 27),
                            rect[0][1] + ((interior_size - h) / 2) - 35),
                            crossword.board[i][j][:-1], font = font_small ,fill="black"
                        )
                if len(crossword.board[i][j]) == 1:
                    w, h = draw.textsize(crossword.board[i][j].upper(), font=font)
                    draw.text(
                        (rect[0][0] + (((interior_size - w) / 2)),
                        rect[0][1] + ((interior_size - h) / 2)),
                        crossword.board[i][j].upper(), font = font ,fill="black"
                    )
                else:
                    w, h = draw.textsize(crossword.board[i][j][-1:].upper(), font=font)
                    draw.text(
                        (rect[0][0] + (((interior_size - w) / 2)),
                        rect[0][1] + ((interior_size - h) / 2)),
                        crossword.board[i][j][-1:].upper(), font = font ,fill="black"
                    )
    print("filled image generated")
    print(img.size)
    img.save('./static/filled_crossword.png')


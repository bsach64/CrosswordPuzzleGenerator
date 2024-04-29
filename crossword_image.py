from PIL import Image, ImageDraw, ImageFont
import logging


def empty_crossword(board: list[list[str]]):
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    img = Image.new(
        "RGBA", (len(board[1]) * cell_size, len(board) * cell_size), "black"
    )
    font = ImageFont.truetype(r"OpenSans-Regular.ttf", 30)
    draw = ImageDraw.Draw(img)
    for i in range(len(board)):
        for j in range(len(board[i])):
            rect = [
                (j * cell_size + cell_border, i * cell_size + cell_border),
                ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border),
            ]
            if board[i][j] != " ":
                draw.rectangle(rect, fill="white")
            if len(board[i][j]) > 1:
                w, h = draw.textsize(board[i][j][:-1], font=font)
                draw.text(
                    (
                        rect[0][0] + (((interior_size - w) / 2) - 27),
                        rect[0][1] + ((interior_size - h) / 2) - 35,
                    ),
                    board[i][j][:-1],
                    font=font,
                    fill="black",
                )
    logging.info("Empty Image Generated!")
    img.save("./static/crossword_board.png")


def filled_crossword(board: list[list[str]]):
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    img = Image.new(
        "RGBA", (len(board[1]) * cell_size, len(board) * cell_size), "black"
    )
    font_small = ImageFont.truetype(r"OpenSans-Regular.ttf", 30)
    font = ImageFont.truetype(r"OpenSans-Regular.ttf", 55)
    draw = ImageDraw.Draw(img)

    for i in range(len(board)):
        for j in range(len(board[i])):
            rect = [
                (j * cell_size + cell_border, i * cell_size + cell_border),
                ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border),
            ]
            if board[i][j] != " ":
                draw.rectangle(rect, fill="white")
                if len(board[i][j]) > 1:
                    w, h = draw.textsize(board[i][j][:-1], font=font_small)
                    draw.text(
                        (
                            rect[0][0] + (((interior_size - w) / 2) - 27),
                            rect[0][1] + ((interior_size - h) / 2) - 35,
                        ),
                        board[i][j][:-1],
                        font=font_small,
                        fill="black",
                    )
                if len(board[i][j]) == 1:
                    w, h = draw.textsize(board[i][j].upper(), font=font)
                    draw.text(
                        (
                            rect[0][0] + ((interior_size - w) / 2),
                            rect[0][1] + ((interior_size - h) / 2),
                        ),
                        board[i][j].upper(),
                        font=font,
                        fill="black",
                    )
                else:
                    w, h = draw.textsize(board[i][j][-1:].upper(), font=font)
                    draw.text(
                        (
                            rect[0][0] + ((interior_size - w) / 2),
                            rect[0][1] + ((interior_size - h) / 2),
                        ),
                        board[i][j][-1:].upper(),
                        font=font,
                        fill="black",
                    )
    logging.info("Filled Image Generated!")
    img.save("./static/filled_crossword.png")

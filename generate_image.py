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
    #img = img.resize((595,530), Image.LANCZOS)
    width = img.size[0]
    height = img.size[1]
    scale_factor = 595/img.size[0]
    img = img.resize((int(width * scale_factor),int(height * scale_factor)), Image.LANCZOS)
    print("image empty generated")
    img.save('crossword_board.png')
    img.save('./static/crossword_board.png')

def filled_crossword(crossword):
    cell_size = 100
    cell_border = 2
    interior_size = cell_size - 2 * cell_border
    # Create a blank canvas
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
    img.save('filled_crossword.png')
    img.save('./static/filled_crossword.png')
    
def pdf_creater():
    img=Image.open("./crossword_board.png")
    file=open("hints.txt", "r+")
    file.readline()
    print(file)
    f= FPDF()
    '''f.add_page()
    f.set_font('Arial',size=30)
    f.text(60,20,txt='Crossword Puzzle')
    f.image('crossword_board.png',0,30)'''
    f.add_page()
    y=20
    f.set_font('Arial',size=12)
    for i in file:
        i=str(i)
        print(i)
        if i=='Across\n' or i == "Down\n":
            f.set_font('Arial',size=30)
            f.text(10,y,txt=i)
        else:
            f.set_font('Arial',size=15)
            f.text(10,y,txt=i)
        y+=15
    f.output('crossword_pdf.pdf')

def pdf2img():
    import fitz
    pdffile = "crossword_pdf.pdf"
    doc = fitz.open(pdffile)
    page = doc.load_page(0)  # number of page
    pix = page.get_pixmap()
    output = "hints.png"
    pix.save(output)
    pix.save("static/hints.png")
    doc.close()



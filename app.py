from flask import Flask,request,render_template
from intro import * 
def mains(n):
    generate.generate_words(n)
    generate.generate_hints()
    words = get_words("crossword.json")
    print("Generating Crossword...")
    crossword = best_board(words, 1000)
    empty_crossword(crossword)
    filled_crossword(crossword)
    with open("crossword.json") as file:
        hints = {}
        hints = json.load(file)
    with open("hints.txt", "w") as file:
        file.write("\nAcross Words\n")
        for word in crossword.info:
            if crossword.info[word].direction == "h":
                line = str(crossword.info[word].order) + ". " + hints[word] + "\n"
                file.write(line)
        file.write("Down Words\n")
        for word in crossword.info:
            if crossword.info[word].direction == "v":
                line = str(crossword.info[word].order) + ". " + hints[word] + "\n"
                file.write(line)
    pdf_creater()
    pdf2img()


app= Flask(__name__)

@app.route("/",)
def index():
    return render_template("index.html")

@app.route("/puzzle", methods=['POST'])
def puzzle():
    n = request.form.get("name","ohhyeah")
    mains(int(n))
    h='''m'''
    return render_template("puzzle.html", name = h)

@app.route("/filled",)
def filled():
    return render_template("filled.html")

app.run(debug=True)
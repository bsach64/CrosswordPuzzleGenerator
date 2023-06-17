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
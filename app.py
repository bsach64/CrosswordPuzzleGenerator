from flask import Flask, request, render_template
from generator import maker
import random

app = Flask(__name__)
OPTIONS = [
    "random",
    "number"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puzzle", methods=['POST', 'GET'])
def puzzle():
    if request.method == "POST":
        option = request.form.get("options")
        if option in OPTIONS:
            if option == "random":
                number = random.randint(10, 20)
            elif option == "number":
                number = int(request.form.get("given_number"))
                print(number)
            hints = maker(number)
            return render_template("puzzle.html", hints=hints)
        else:
            return render_template("invalid.html")
    return render_template("index.html")

@app.route("/filled", methods=['POST', 'GET'])
def filled():
    return render_template("filled.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4444)
from flask import Flask, request, render_template
from generator import maker
import random

app = Flask(__name__)

OPTIONS: list[str] = [
    "random",
    "number",
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/puzzle", methods=['POST', 'GET'])
def puzzle():
    if request.method == "POST":
        option: str | None = request.form.get("options")
        if option not in OPTIONS:
            return render_template("invalid.html")
        hints: list[str] = []
        if option == "random":
            number: int = random.randint(10, 20)
            hints = maker(number)
        elif option == "number":
            n_str, n = str(request.form.get("given_number")), 0
            try:
                n = int(n_str)
            except ValueError:
                ...
            hints = maker(n)
        return render_template("puzzle.html", hints=hints)
    return render_template("index.html")

@app.route("/filled", methods=['POST', 'GET'])
def filled():
    return render_template("filled.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

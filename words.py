import json

Intro = "Enter the list of words and press ctrl+D to stop."
print(Intro)

words = {}

while True:
    try:
        words[input("Word: ")] = ""
    except EOFError:
        print()
        break

with open("crossword.json", "w") as file:
    json.dump(words, file)
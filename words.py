import json

def main():
    input_words()

def input_words():
    words = input("Enter the list of words separated by spaces: ")
    words = words.split(" ")

    crossword = {}

    for word in words:
        crossword[word] = ""

    with open("crossword.json", "w") as file:
        json.dump(crossword, file)

if __name__ == "__main__":
    main()
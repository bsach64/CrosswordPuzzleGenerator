import json
import generate
import words
import os


def main_screen():
    # os.system("cls")
    print("""
    Welcome to Cross_Word_Generator


        1> Prompt words through OpenAI
        2> Input words manually

        """)
    c=int(input("\tEnter your choice: "))

    if c==1:
        generate.generate_words()
    elif c==2:
        words.input_words()
    print_words()
    c=input("Do you want move further with the words and generate hints? (y/n)")
    if c=="y" or c == "Y":
        generate.generate_hints()
    else:
        main_screen()

def print_words():
    with open("crossword.json") as file:
        crossword = json.load(file)
    os.system('cls')
    print("Listed words:")
    for i in crossword:
        print(i)

def print_hints():
    with open("crossword.json") as file:
        crossword = json.load(file)
    print(crossword)

def main():
    main_screen()

if __name__ == "__main__":
    main_screen()
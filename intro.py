import json
import generate
from words import input_words, get_words
import os
from best import best_board
from generate_image import empty_crossword

def main_screen():
    print("""
    Welcome to Cross_Word_Generator


        1> Prompt words through OpenAI
        2> Input words manually

        """)
    while True:
        try:
            choice =int(input("\tEnter your choice: "))
            if choice > 2 or choice < 0:
                print("\tNot in Range")
            else:
                break
        except ValueError:
            print("Enter a valid Integer")
    if choice == 1:
        generate.generate_words()
    elif choice == 2:
        input_words()
    print_words()
    choice = input("Do you want move further with the words and generate hints? (y/n)")
    if choice == "y" or choice == "Y":
        generate.generate_hints()
        print_hints()
        words = get_words("crossword.json")
        print("Generating Crossword...")
        crossword, placed_words = best_board(words, 1000)
        for line in crossword:
            print(line)
        print(placed_words)
        empty_crossword(crossword)
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
    for key, value in crossword.items():
        print(key, ' : ', value)
    print()

def main():
    main_screen()

if __name__ == "__main__":
    main_screen()
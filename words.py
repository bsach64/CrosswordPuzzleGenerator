Intro = "Enter the list of words and press ctrl+D to stop."
print(Intro)

with open("words.txt", "a") as file:
    while True:
        try:
            word = input("Word: ")
            file.write(word+"\n")
        except EOFError:
            print()
            break
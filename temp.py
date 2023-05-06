def generate_words():
    while True:
        try:
            n = int(input("Number of words to generate (three or more): "))
            break
        except ValueError:
            ...
    print("Generating Words...")
    with open("api_key.txt") as file:
        file_content = file.readline()
        api_key = file_content

    openai.api_key = api_key

    prompt = f"generate {n} words for a crossword puzzle."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    raw_answer = str(response["choices"][0]["text"])
    raw_answer = raw_answer.replace('\n','')
    raw_answer = raw_answer.replace('.','')    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in numbers:
        if str(number) in raw_answer:
            raw_answer = raw_answer.replace(str(number), '')
    words = raw_answer.strip().split(" ")

    crossword = {}
    for word in words:
        crossword[word.lower()] = ""

    with open("crossword.json", "w") as file:
        json.dump(crossword, file)

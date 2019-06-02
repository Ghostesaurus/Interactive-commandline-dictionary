import json
import difflib

data:dict = json.load(open("data.json"))

def translate(word:str):
    w = word.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    else:
        return None 
    # we can ommit the else statement because None is the default value returned 
    # when no return statement is assigned

def check_similar_word(word:str):
    w = word.lower()
    # return difflib.get_close_matches(w, data.keys(), 1, 0.85)
    # we will return the first array results beacuse it is sorted by the highest cutoff first
    return difflib.get_close_matches(w, data.keys())[0]

def print_multiple_lines(mylist:list):
    for item in mylist:
        print(item)

def main():
    userInput:str = input("Enter a word to translate: ")
    translations:str = translate(userInput)
    if translations == None:
        similar_word:list = check_similar_word(userInput)
        if not similar_word:
            print("This word doesn't have a translation in our data, please check that the word is correct")
        else:
            print("{} {}?".format("This word seems incorrect, did you mean", similar_word))
            user_question_input:str = input("If yes press Y, if no press any key to continue: ")
            if user_question_input.lower() == "y":
                print_multiple_lines(translate(similar_word))
                print()
    else:
        print_multiple_lines(translations)
        print()

while True:
    main()

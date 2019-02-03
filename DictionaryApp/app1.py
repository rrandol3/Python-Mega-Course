import json
from difflib import get_close_matches

data = json.load(open("data.json"))

userinput = input("Enter a word to search for: ")

def format_definition_output(definitions):
    num = 0
    formatteddefinitions = ""
    for item in definitions:
        num = num + 1
        formatteddefinitions = formatteddefinitions + str(num) + ": " + item + "\n"
    return formatteddefinitions

def get_word_definition(word):
    word = word.lower()
    if word in data:
        return format_definition_output(data[word])
    elif word.title() in data:
        return format_definition_output(data[word.title()])
    elif word.upper() in data:
        return format_definition_output(data[word.upper()])
    else:
        possible_matches = get_close_matches(word, data)
        if  len(possible_matches) > 0:
            answer = input("Did you mean " + possible_matches[0] +"? Enter Y for Yes and N for No ")
            if answer == "Y":
                return  get_word_definition(possible_matches[0])
            else:
                newsearch = input("Enter a word to search for: ")
                print(get_word_definition(newsearch))
        else:
            return "Cannot find that word!"

print(get_word_definition(userinput))

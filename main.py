import json
import difflib


data = json.load(open("data.json"))

# print(data)

def get_def(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        similar = difflib.get_close_matches(word, data.keys())
        if similar:
            suggest = similar[0]
            return f"not found. search for '{suggest}'?"
        else:
            return "sorry!!"
        


test = input("what are you searching for? : ")

for word in test:
     define = get_def(word)
print(f"definition of '{word}': {define}")
print(f"definition of '{word}': {define}")

#print(test)

import json
import difflib

# Load the JSON data into a Python dictionary
with open("data.json", "r") as file:
    dictionary_data = json.load(file)

# Function to return the definition of a word
def get_definition(word):
    # Convert the word to lowercase for case insensitivity
    word = word.lower()
    # Check if the word is in the dictionary
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        # If the word is not found, suggest similar words
        similar_words = difflib.get_close_matches(word, dictionary_data.keys())
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Sorry, the word was not found in the dictionary."

# Test cases
test_words = ["apple", "Banana", "OrAnGe", "grapes", "pinaple", "mango"]

for word in test_words:
    definition = get_definition(word)
    print(f"Definition of '{word}': {definition}")

import re

def text_match(text):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, text):
        return 'Found a match'
    else:
        return "Not found any match"


print(text_match(str(input("Enter a string\n"))))
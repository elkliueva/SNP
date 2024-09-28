import re

def is_palindrome(string):
    string = str(string)
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()

    return cleaned_string == cleaned_string[::-1]

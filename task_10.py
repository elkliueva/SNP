import re

def count_words(string):

    string = string.lower()
    string = re.sub(r'[^a-z\s]', ' ', string)
    words = string.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def break_words(stuff):
    words = stuff.split(" ")
    return words

print(break_words("rohit kumar sinha"))

def sort_words(words):
    return sorted(words)

print(sort_words("rohit"))

def print_first_word():
    word = "my name is rohit sinha".pop(0)
    print(word)

print_first_word()

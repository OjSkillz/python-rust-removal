def read_file(path):
    with open(path, "r") as file:
        return file.read()

def clean_text(text):
    text.replacce(["!",":",";",",",".","?"], " ").lower().split("")
    return text

def count_words(words):
    for word in words:
        print(f"{word} : {words.count(word)}")
        counter = {word: words.count(word)}
        return counter
    return
def print_top_words(counter, limit=10):
    ...

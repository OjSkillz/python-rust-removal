from click import help_option


def read_file(path):
    with open(path, "r") as file:
        return file.read()

def clean_text(file):
    file = file.lower().split()
    for word in file:
        if word[::-1] in [",",".",":","!","?"]:
            word[::-1] = ""
    print(file)
    return file

def count_words(words):
    for word in words:
        print(f"{word} : {words.count(word)}")
        counter = {word: words.count(word)}
        return counter
    return None


def print_top_words(counter, limit=10):
    for word, count in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:limit]:
        print(f"{word}: {count}")

file_path = input("Enter the file path: ")
read_text = read_file(file_path)
print(read_text)
cleaned_text = clean_text(read_text)
count_words(cleaned_text)
print_top_words(count_words(clean_text(read_text)))
from click import help_option


def read_file(path):
    with open(path, "r") as file:
        return file.read()

def clean_text(file):
    file = file.lower().split()
    for i, w in enumerate(file):
      file[i] = w.strip(".,!?:;")
    return file

def count_words(words):
    counter = {}
    for word in words:
        counter[word] = words.count(word)
    return counter



def print_top_words(counter, limit=10):
    for word, count in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:limit]:
        print(f"{word}: {count}")

file_path = input("Enter the file path: ")
read_text = read_file(file_path)
cleaned_text = clean_text(read_text)
count_words(cleaned_text)
print_top_words(count_words(clean_text(read_text)))
from stats import get_word_count
def get_book_text(file_path):
    contents = None

    with open(file_path) as file:
        contents = file.read()

    return contents

def main():
    file_path = "books/frankenstein.txt"
    contents = get_book_text(file_path)
    word_count = get_word_count(contents)
    print(f"Found {word_count} total words")


main()
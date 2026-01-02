def get_book_text(file_path):
    contents = None

    with open(file_path) as file:
        contents = file.read()

    return contents

def main():
    file_path = "books/frankenstein.txt"
    contents = get_book_text(file_path)
    print(contents)


main()
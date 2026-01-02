import sys
from stats import get_word_count, get_each_character_count, create_sorted_list
def get_book_text(file_path):
    contents = None

    with open(file_path) as file:
        contents = file.read()

    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    try:
        contents = get_book_text(file_path)
    except OSError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    word_count = get_word_count(contents)
    characters_count = get_each_character_count(contents)
    sorted_list = create_sorted_list(characters_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in sorted_list:
        char = char_count["char"]
        count = char_count["num"]

        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


main()
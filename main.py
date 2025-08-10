import sys
from stats import *

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_book_report(filepath):
    book_string = get_book_text(filepath)
    word_count = get_num_words(book_string)
    char_count = string_to_char(book_string)
    char_sorted = sort_high_to_low(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    print_book_report(book_path)

main()
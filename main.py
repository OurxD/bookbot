from sys import argv, exit
from stats import get_words_count, get_char_count, get_sorted_char_list

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = argv[1]

    book_text = get_book_text(path)
    book_word_count = get_words_count(book_text)
    book_char_count_dict = get_char_count(book_text)
    book_sorted_char_list = get_sorted_char_list(book_char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print("--------- Character Count -------")
    for sorted_char in book_sorted_char_list:
        print(f"{sorted_char['char']}: {sorted_char['num']}")
    print("============= END ===============")

main()
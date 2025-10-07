from stats import count_char, sort_letters, count_words
import sys


def main():
    entries = len(sys.argv)
    if(entries < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book = get_book_text(filepath)
        word_count = count_words(book)
        chars = count_char(book)
        sorted_chars = sort_letters(chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print('----------- Word Count ----------')
        print(f"Found {word_count} total words")
        print('--------- Character Count -------')
        for item in sorted_chars:
            letter = item['char']
            num = item['num']
            print(f"{letter}: {num}")
        print('============= END ===============')

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        





main()

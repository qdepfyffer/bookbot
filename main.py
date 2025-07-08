from stats import get_num_words, get_char_freq, get_sorted_list
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()

def pretty_print(elements: list[dict]) -> None:
    for element in elements:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

def main() -> None:

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = (get_num_words(text))
    freq = get_char_freq(text)
    sorted_list = get_sorted_list(freq)

    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    pretty_print(sorted_list)

    print("============= END ===============")

main()
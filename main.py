ALPHABET = {
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
}


def main():
    with open("./books/frankenstein.txt") as f:
        book = f.read()

        print_report(book)


def count_words(book: str) -> int:
    words = book.split()
    word_count = len(words)

    return word_count


def count_chars(book: str) -> dict[str, int]:
    count = {}

    for c in book.lower():
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count


def print_report(book: str):
    print('--- Begin report of "books/frankenstein.txt" ---')

    words = count_words(book)
    chars = count_chars(book)
    letters = filter(lambda c: c in ALPHABET, chars.keys())

    print(f"{words} words found in the document\n")

    for l in sorted(letters, key=lambda l: chars[l], reverse=True):
        print(f"The '{l}' character was found {chars[l]} times")

    print("--- End report ---")


main()

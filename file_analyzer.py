import string
import os
import argparse


def remove_punc(input_str):
    translator = str.maketrans('', '', string.punctuation)
    return input_str.translate(translator)


def get_args():
    parser = argparse.ArgumentParser(description="Text File Analyzer")

    parser.add_argument(
        "filepath",
        help="Path to the text file you want to analyze"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top common words to display (default = 5)"
    )

    return parser.parse_args()


def analyze_file(filepath, top_n):

    filepath = os.path.normpath(filepath)

    if not os.path.exists(filepath):
        print("File not found!")
        return

    with open(filepath, "r") as file:
        text = file.read()

    cleaned_text = remove_punc(text.lower())

    # Count chars
    characters = list(cleaned_text)
    print("Character count:", len(characters))

    # Count Lines
    lines = cleaned_text.split("\n")
    print("Line count:", len(lines))

    # Count words
    words = cleaned_text.split()
    print("Word count:", len(words))

    # Word frequency count
    word_dict = {}
    ignored_words = {"the", "and", "is", "in", "of", "to", "a", "an"}

    for item in words:
        if item not in ignored_words:
            word_dict[item] = word_dict.get(item, 0) + 1

    print("There are", len(word_dict), "unique words (excluding common words)")

    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    print(f"\nTop {min(top_n, len(sorted_dict))} most common words:")
    for i in range(min(top_n, len(sorted_dict))):
        word, count = sorted_dict[i]
        print(f'{i + 1}. "{word}" appears {count} times')


if __name__ == "__main__":
    args = get_args()
    analyze_file(args.filepath, args.top)

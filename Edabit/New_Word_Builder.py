"""
Create a function that builds a word from the scrambled letters contained in the first list. Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).

Examples
word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"
"""


def main(chars, order):
    ordered_char_holder = [0 for i in range(len(chars))]

    for o, c in zip(order, chars):
        ordered_char_holder[o] = c

    return "".join(ordered_char_holder) 


if __name__ == "__main__":
    res = main(["g", "e", "o"], [1, 0, 2])
    print(res)
    res = main(["e", "t", "s", "t"], [1, 0, 2, 3])
    print(res)

import random

def pig_latin_game(word):
    vowels = ["a", "e", "i", "o", "u"]
    postfix = random.sample(["yay", "way"], 1)
    if word[0] in vowels:
        word += postfix
    else:
        word = word[1:] + word[0]
        word += "ay"

    return word


if __name__ == "__main__":
    word = "apple"
    res = pig_latin_game(word)
    print(res)
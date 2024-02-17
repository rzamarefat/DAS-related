def alphabet_shift(string):
    res = ""
    for char_ in string:
        if char_.isalpha():
            if char_ == "a":
                res += "z"
            elif char_ == "A":
                res += "Z"
            else:
                res += chr(ord(char_) + 1)

    print(res)


if __name__ == "__main__":
    string = "aft"
    alphabet_shift(string)
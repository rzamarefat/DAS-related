def find_first_digit(string):
    for char in string:
        if char.isdigit():
            return char

    return "There is no digit in the given sttring"

if __name__ == "__main__":
    res = find_first_digit("anbr")

    print(res)
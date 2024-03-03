def longest_digit_prefix(string):
    digit_prefix = ""
    for char in string:
        if char.isdigit():
            digit_prefix += char
        else:
            return digit_prefix
    
    return digit_prefix


if __name__ == "__main__":
    res = longest_digit_prefix("12543")
    print(res)
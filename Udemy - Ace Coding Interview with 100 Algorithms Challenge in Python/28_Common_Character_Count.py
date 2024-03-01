def find_common_char_count(string1, string2):
    common_chars = []
    for char in string1:
        if char in string2:
            common_chars.append(char)

    return len(set(common_chars))


if __name__ == "__main__":
    string1 = "apple"
    string2 = "orange"
    res = find_common_char_count(string1, string2)

    print(res)
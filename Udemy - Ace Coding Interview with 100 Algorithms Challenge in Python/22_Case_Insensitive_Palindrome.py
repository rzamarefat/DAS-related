def case_insensitive_palindrome(string):
    reversed_string = ""
    for index in range(len(string)):
        reversed_string += string.lower()[len(string) - index - 1]

    if reversed_string == string.lower():
        return True
    return False

if __name__ == "__main__":
    res = case_insensitive_palindrome("Lot")
    print(res)
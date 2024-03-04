def find_first_missing_letter(string):
    last_char_ord = ord(string[0])
    for char in string[1:]:
        if ord(char) == last_char_ord + 1:
            last_char_ord += 1
        else:
            return chr(ord(char) - 1)
    
    return "No missing letter"

        


if __name__ == "__main__":
    res = find_first_missing_letter(string="abcdf")
    print(res)
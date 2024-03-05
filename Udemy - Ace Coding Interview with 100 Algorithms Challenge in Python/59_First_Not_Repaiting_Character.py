def find_first_not_repeating_char(string):
    checked = []
    for index, char in enumerate(string):
        if index + 1 >= len(string):
            if char in checked:
                return "Nothing"
            else:
                return string[-1]
        if not(char == string[index+1]) and not(char in checked):
            return char
        
        checked.append(char)



if __name__ == "__main__":
    res = find_first_not_repeating_char("aabbccdd")
    print(res)

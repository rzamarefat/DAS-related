def sum_of_two(string):
    if len(string) < 2:
        return "The string must contain at least two digits"
    
    sum_ = 0
    for char in string:
        if not(char.isdigit()):
            return "The string must include only numerical digits"
        sum_ += int(char)

    return sum_

if __name__ == "__main__":
    res = sum_of_two("54s")
    print(res)
        

def find_if_contain_only_even_integers(number):
    for char in str(number):
        if not(int(char) % 2 == 0):
            return "The number provided does not contain only even integers"
        
    return "The number provided contains only even integers"




if __name__ == "__main__":
    res = find_if_contain_only_even_integers(256)
    print(res)
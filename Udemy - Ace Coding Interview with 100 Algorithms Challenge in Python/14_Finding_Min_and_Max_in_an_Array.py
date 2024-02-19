def find_min_max_in_array(array):
    min_value = float("+inf")
    max_value = float("-inf")
    
    for a in array:
        if a < min_value:
            min_value = a
        
        if max_value < a:
            max_value = a

    return min_value, max_value

if __name__ == "__main__":
    min_, max_ = find_min_max_in_array([-11,1,1, 5, 6, 10])

    print(min_, max_)
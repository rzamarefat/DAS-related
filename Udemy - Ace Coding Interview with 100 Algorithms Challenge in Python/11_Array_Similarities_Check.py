def check_two_arrays_similarity(array_1, array_2):
    if len(array_1) != len(array_2):
        return False
    
    array_1 = sorted(array_1)
    array_2 = sorted(array_2)

    for a1, a2 in zip(array_1, array_2):
        if a1 != a2:
            return False
    
    return True
    

if __name__ == "__main__":
    array_1 = [1,2,3,4,5]
    array_2 = [2,1,3,4,6]
    res = check_two_arrays_similarity(array_1, array_2)
    print(res)
    
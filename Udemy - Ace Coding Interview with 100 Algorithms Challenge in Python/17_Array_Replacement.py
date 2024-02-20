def array_replacement(arr, target, replacement):
    if not(target in arr):
        return array
    
    for index, e in enumerate(arr):
        if e == target:
            arr[index] = replacement

    return arr

if __name__ == "__main__":
    array = [1, 4, 5, 10, 9, 8]
    target = 4
    replacement = 11
    res = array_replacement(array, target, replacement)

    print(res)
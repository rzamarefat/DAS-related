def flatten_array(arr):
    flattened_array = []
    for a in arr:
        if isinstance(a, list):
            for e in a:
                flattened_array.append(e)
        else:
            flattened_array.append(a)
            
    return flattened_array

if __name__ == "__main__":
    arr = [[1,2,3], [4,5,6], 3, 4, [1]]
    res = flatten_array(arr)
    print(res)
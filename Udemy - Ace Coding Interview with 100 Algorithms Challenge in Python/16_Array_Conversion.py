def array_conversion(array):
    return [str(e) for e in array]


if __name__ == "__main__":
    arr = [1, 4, 5, 6, 7]
    res = array_conversion(arr)
    print(res)
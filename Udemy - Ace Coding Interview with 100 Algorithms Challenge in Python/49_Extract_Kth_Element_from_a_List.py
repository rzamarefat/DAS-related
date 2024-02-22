def extract_kth_element(arr, k):
    if not(k in arr):
        return arr

    res = []
    for index, e in enumerate(arr):
        if e == k:
            return arr[0:index] + arr[index+1:]

    


if __name__ == "__main__":
    arr = [21, 33, 67, 54, 34]
    k = 33
    res = extract_kth_element(arr, k)

    print(res)
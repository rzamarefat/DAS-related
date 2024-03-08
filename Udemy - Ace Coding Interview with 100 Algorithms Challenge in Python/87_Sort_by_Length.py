# def sort_by_length(arr):
#     return sorted(arr, key=len)

def sort_by_length(arr):
    sorted_arr = [arr[0]]

    for word in arr[1: ]:
        if len(word) < len(sorted_arr[-1]):
            sorted_arr.insert(0, word)
        else:
            sorted_arr.append(word)

    return sorted_arr


if __name__ == "__main__":
    res = sort_by_length(["apple", "banana", "cherry", "date", "elderberry"])
    print(res)
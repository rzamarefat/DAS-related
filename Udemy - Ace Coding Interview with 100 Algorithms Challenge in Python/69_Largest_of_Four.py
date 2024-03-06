def find_largest_of_four(arrays):
    return [max(arr) for arr in arrays]


if __name__ == "__main__":
    arrays = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    res = find_largest_of_four(arrays)

    print(res)
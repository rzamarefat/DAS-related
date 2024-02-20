def find_duplicates(arr):
    dup_holder = []
    checked_elements = []
    for a in arr:
        if not(a in checked_elements):
            checked_elements.append(a)
        else:
            dup_holder.append(a)

    return dup_holder


if __name__ == "__main__":
    res = find_duplicates([1, 3, 2,2,9, 9, 10, 8])

    print(res)


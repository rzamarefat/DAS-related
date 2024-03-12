def find_if_contains_close_numbers(numbers, threshold):
    for index1, i in enumerate(numbers):
        for index2, j in enumerate(numbers):
            if abs(i - j) <= threshold and not(index1 == index2):
                print(i, j)
                return "Contains"
    return "Does Not Contain"


if __name__ == "__main__":
    threshold = 1
    res = find_if_contains_close_numbers([7, 12, 15, 21, 24, 31], threshold)
    print(res)
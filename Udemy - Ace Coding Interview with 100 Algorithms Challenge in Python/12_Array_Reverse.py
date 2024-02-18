# def reverse_array(array):
#     return array[::-1]


def reverse_array(array):
    res = []

    for index in range(len(array)):
        res.append(array[len(array) - index -1])
    return res

if __name__ == "__main__":
    array = [1, 4, 6, 7]
    res = reverse_array(array)
    print(res)
def find_closest_pair(arr, target_number):
    min_distance = float("+inf")

    for index, a in enumerate(arr):
        for index_, a_ in enumerate(arr):
            if not(index_ == index):
                distance = abs(index - index_)
                if a + a_ == target_number and min_distance > distance:
                    min_distance = abs(distance)

    
    return min_distance



if __name__ == "__main__":
    arr = [1,3,6,7,5,9,]
    target_number = 8
    res = find_closest_pair(arr, target_number)

    print(res)

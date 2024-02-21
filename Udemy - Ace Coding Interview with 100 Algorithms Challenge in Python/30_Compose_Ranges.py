def compose_ranges(arr):
    valid_range = []
    last_holder = None

    flag = True
    for index, e in enumerate(arr):
        if not(index + 1 >= len(arr)):
            diff_with_next_element = array[index+1] - e

            if diff_with_next_element == 1 or diff_with_next_element == -1:
                valid_range.append(arr[index])
            else:
                if flag:
                    last_holder = e, index
                    valid_range.append(e)
                    flag = False

    valid_range_start = valid_range[0]
    valid_range_end = valid_range[-1]
    print([f"{valid_range_start} -> {valid_range_end}"]+ [f for f in arr[last_holder[1]+1:]])



if __name__ == "__main__":
    array = [7,6,5,4,3,2,5,8,6]
    # array = [1,2,3,4,5,6,1,4,7,2,4]
    compose_ranges(array)
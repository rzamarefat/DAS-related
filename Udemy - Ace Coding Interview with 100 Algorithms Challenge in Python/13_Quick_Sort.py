def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]

        less_than_pivot = [e for e in array[1:] if e < pivot]
        greater_than_pivot = [e for e in array[1:] if e >= pivot]

        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


    

if __name__ == "__main__":
    array = [1, 4, 7, 2, 0, 7, 5, 9]
    res = quick_sort(array)
    print(res)
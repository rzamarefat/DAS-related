"""
- Start from the beginning of the list.
- Compare each pair of adjacent elements.
- If the elements are in the wrong order, swap them.
- Move to the next pair of elements.
- Repeat steps 2-4 until the end of the list is reached.
- After the first pass, the largest element is guaranteed to be at the end of the list.
- Repeat steps 1-6 for the remaining unsorted portion of the list.
"""

def do_bubble_sort(arr):
    n = len(arr)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1],  arr[j]

    return arr


if __name__ == "__main__":
    arr = [1, 5, 2, 4, 10, 1, 3, 6]
    sorted_arr = do_bubble_sort(arr)

    print(sorted_arr)
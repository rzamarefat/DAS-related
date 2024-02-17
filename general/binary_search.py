"""
binary search
- Start with the entire sorted list.
- Compare the target element with the middle element of the current range.
- If the target is equal to the middle element, the search is successful, and you've found the target.
- If the target is less than the middle element, repeat the search in the lower half of the current range.
- If the target is greater than the middle element, repeat the search in the upper half of the current range.
- Continue dividing the search range in half and repeating the process until the target is found or the range becomes empty.
"""


def binary_search(array, target):
    low_idx, high_idx = 0, len(arr) - 1

    while low_idx <= high_idx:
        
        mid = (low_idx + high_idx) // 2
        
        if array[mid] == target:
            return mid
        elif target < array[mid]:
            high_idx = high_idx // 2 - 1
        else:
            low_idx = high_idx // 2 + 1
        
    return -1 #There is no such target element in the array


if __name__ == "__main__":
    arr = [1, 4, 6, 10, 19, 21]
    target = 4
    res = binary_search(arr, target)
    print(res)
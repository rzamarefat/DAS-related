"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True

consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False

consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False

consecutive_combo([44, 46], [45]) ➞ True
"""

def main(array1, array2):
    combined_array = array1 + array2

    min_ = min(combined_array)
    max_ = max(combined_array)


    for i in range(min_, max_+1):
        if not(i in combined_array):
            return False
    
    return True

if __name__ == "__main__":
    res = main([7, 4, 5, 1], [2, 3, 6])
    print(res == True)

    res = main([1, 4, 6, 5], [2, 7, 8, 9])
    print(res == False)

    res = main([1, 4, 5, 6], [2, 3, 7, 8, 10])
    print(res == False)

    res = main([44, 46], [45])
    print(res == True)
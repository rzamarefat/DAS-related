"""
Given an array of elements of length n, ranging from 0 to n - 1. 
All elements may not be present in the array. If the element is not present then there will be -1 present in the array. 
Rearrange the array such that arr[i] = i and if i is not present, display -1 at that place.

Examples: 

Input: arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
Explanation: In range 0 to 9, all except 0, 5, 7 and 8 are present. Hence, we print -1 instead of them.


Input: arr[] = [0, 1, 2, 3, 4, 5] 
Output: [0, 1, 2, 3, 4, 5]
Explanation: In range 0 to 5, all number are present.


https://www.geeksforgeeks.org/rearrange-array-arri/
"""

# First Solution
def main(array):
    n = len(array)
    answer_holder = []

    for i in range(n):
        if i not in array:
            answer_holder.append(-1)
        else:
            answer_holder.append(i)

    return answer_holder

# Second Solution More Efficient
def main(array):
    temp_arr = [-1] * len(array)

    for i in range(len(array)):
        if array[i] != -1:
            temp_arr[array[i]] = array[i]

    return temp_arr


if __name__ == "__main__":
    ar = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
    res = main(ar)
    print(res)
"""
Given an array of integers. All numbers occur twice except one number which occurs once. Find the number in O(n) time & constant extra space.

Example : 

Input:  arr[] = {2, 3, 5, 4, 5, 3, 4}
Output: 2 


Input:  arr[] = {2, 5, 2}
Output: 5


Input:  arr[] = {3}
Output: 3
"""

def main(arr):
    frequency_holder = {}

    for element in arr:
        frequency_holder[element] = frequency_holder.get(element, 0)+1

    for k,v in frequency_holder.items():
        if v == 1:
            return k
            
    return -1


if __name__ == "__main__":
    arr = [2, 3, 5, 4, 5, 3, 4]
    res = main(arr)

    print(res)
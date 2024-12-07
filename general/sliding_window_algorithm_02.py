"""
2. Smallest Subarray with Sum Greater Than or Equal to S
Problem: Given an array of positive integers arr and a positive integer S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists.

Input: arr = [2, 1, 5, 2, 3, 2], S = 7

Output: 2

Explanation: The subarray [5, 2] has a sum of 7 and is the smallest possible subarray.

Difficulty: Medium
"""


def main(arr, s):
    window_sum_total = 0
    min_length = float('inf')
    window_start_index = 0

    for window_end_index in range(len(arr)):
        window_sum_total += arr[window_end_index]
        while window_sum_total >= s:
            min_length = min(min_length, window_end_index - window_start_index + 1)
            window_sum_total -= arr[window_start_index]
            window_start_index += 1

    return 0 if min_length == float('inf') else min_length
        

if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    res = main(arr, k)
    print(res)
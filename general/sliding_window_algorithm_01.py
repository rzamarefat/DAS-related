"""
1. Maximum Sum Subarray of Size K
Problem: Given an array of integers arr and a positive integer k, find the maximum sum of any contiguous subarray of size k.

Input: arr = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Difficulty: Easy
"""


def main(arr, k):
    max_sum_total = 0
    window_start_index = 0
    window_sum_total = 0


    for window_end_index in range(len(arr)):
        window_sum_total += arr[window_end_index]
        print(window_end_index, window_sum_total)

        if window_end_index >= k-1:
            max_sum_total = max(max_sum_total, window_sum_total)

            window_sum_total -= arr[window_start_index]

            window_start_index += 1

    return max_sum_total


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    res = main(arr, k)
    print(res)
"""
1. Maximum Sum Subarray of Size K
Problem: Given an array of integers arr and a positive integer k, find the maximum sum of any contiguous subarray of size k.

Input: arr = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Difficulty: Easy
"""


def main(arr, s):
    window_start_index = 0
    max_length = 0
    char_index_map = {}

    for window_end_index in range(len(s)):
        right_char = s[window_end_index]

        if right_char in char_index_map:
            window_start_index = max(window_start_index, char_index_map[right_char] + 1)

        char_index_map[right_char] = window_end_index
        max_length = max(max_length, window_end_index - window_start_index + 1)

    return max_length


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    res = main(arr, k)
    print(res)
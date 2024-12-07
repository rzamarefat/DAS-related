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
    char_frequency = {}

    for window_end_index in range(len(s)):
        right_char = s[window_end_index]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while len(char_frequency) > k:
            left_char = s[window_start_index]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start_index += 1

        max_length = max(max_length, window_end_index - window_start_index + 1)

    return max_length


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    res = main(arr, k)
    print(res)
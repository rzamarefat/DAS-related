"""
1. Maximum Sum Subarray of Size K
Problem: Given an array of integers arr and a positive integer k, find the maximum sum of any contiguous subarray of size k.

Input: arr = [2, 1, 5, 1, 3, 2], k = 3

Output: 9

Explanation: The subarray [5, 1, 3] has the maximum sum of 9.

Difficulty: Easy
"""


def main(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    s2_count = [0] * 26

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    window_start = 0
    for window_end in range(len(s1), len(s2)):
        if matches == 26:
            return True

        right_char_index = ord(s2[window_end]) - ord('a')
        s2_count[right_char_index] += 1
        if s1_count[right_char_index] == s2_count[right_char_index]:
            matches += 1
        elif s1_count[right_char_index] + 1 == s2_count[right_char_index]:
            matches -= 1

        left_char_index = ord(s2[window_start]) - ord('a')
        s2_count[left_char_index] -= 1
        if s1_count[left_char_index] == s2_count[left_char_index]:
            matches += 1
        elif s1_count[left_char_index] - 1 == s2_count[left_char_index]:
            matches -= 1

        window_start += 1

    return matches == 26


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    res = main(arr, k)
    print(res)
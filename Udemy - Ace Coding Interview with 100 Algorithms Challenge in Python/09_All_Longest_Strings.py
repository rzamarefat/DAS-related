def find_longest_string_in_array(list_of_strings):
    max_len = float("-inf")
    max_len_string = None
    for string in list_of_strings:
        if max_len < len(string):
            max_len = len(string)
            max_len_string = string

    return max_len_string


if __name__ == "__main__":
    res = find_longest_string_in_array(["ali", "reza", "s"])

    print(res)

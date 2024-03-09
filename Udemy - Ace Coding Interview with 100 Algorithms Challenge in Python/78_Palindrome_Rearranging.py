def rearrange_palindrome(string):
    frequency_data_holder = {}

    for char in string:
        if not(char in frequency_data_holder.keys()):
            frequency_data_holder[char] = 1
        else:
            frequency_data_holder[char] += 1
    

    odd_frquency_chars = [(k,v) for k,v in frequency_data_holder.items() if v % 2 != 0]

    if len(odd_frquency_chars) == 1:
        return "The string can be rearranged to a palindrome."
    else:
        return "The string cannot be rearranged to a palindrome"


if __name__ == "__main__":
    res = rearrange_palindrome("aabbbcccee")
    print(res)
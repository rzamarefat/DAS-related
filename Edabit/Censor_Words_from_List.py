"""
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.

Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"

censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")

censor_string("Why did the chicken cross the road", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****"
"""


def main(string, to_be_censored_lst, replacement_char):
    final_result = "" 
    words = string.split(" ")

    for index, w in enumerate(words):
        if w in to_be_censored_lst:
            censored_word = ""
            for _ in w:
                censored_word += replacement_char
            final_result += censored_word
        else:
            final_result += w
        

        if not(index == len(words) - 1):
            final_result += " "

    # print(final_result)
    return final_result
            



if __name__ == "__main__":
    res = main("Today is a Wednesday!", ["Today", "a"], "-")
    print(res == "----- is - Wednesday!")

    res = main("The cow jumped over the moon.", ["cow", "over"], "*")
    print(res == "The *** jumped **** the moon.")
    
    res = main("Why did the chicken cross the road", ["Did", "chicken", "road"], "*")
    print(res == "Why *** the ******* cross the ****")

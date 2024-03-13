"""
Given a string s consisting of words and spaces, return the length of the last word
"""


def main(s):
    length = 0
    last_word_found = False
    for char in s[::-1]:
        if char.isalpha() or char.isdigit():
            length += 1
            last_word_found = True
        else:
            if last_word_found:
                return length
            
            length = 0

        
    # return length

if __name__ == "__main__":
    res = main("Hello  world I    am a   program in Pythons   ")
    print(res)
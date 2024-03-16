"""
C*ns*r*d Str*ngs
Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"
"""


def main(censored_string, censored_items):
    counter = 0
    uncensored_string=""
    for char in censored_string:
        if char == "*":
            char = censored_items[counter]
            counter += 1

        uncensored_string += char

    return uncensored_string

if __name__ == "__main__":
    res = main("Wh*r* d*d my v*w*ls g*?", "eeioeo")
    print(res)


    res = main("abcd", "")
    print(res)

    res = main("*PP*RC*S*", "UEAE")
    print(res)

    
    
"""
Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"

Examples
encrypt("banana") ➞ "0n0n0baca"

encrypt("karaca") ➞ "0c0r0kaca"

encrypt("burak") ➞ "k0r3baca"

encrypt("alpaca") ➞ "0c0pl0aca"
"""


def main(word):
    replacement_data = {
        "a": 0,
        "e": 1,
        "i": 2,
        "o": 2,
        "u": 3,
    }
    
    result = ""
    for char in [char for char in word[::-1]]:
        if char in replacement_data.keys():
            char = str(replacement_data[char])
        
        result += char
    

    return result + "aca"




if __name__ == "__main__":
    res = main("banana")
    print(res == "0n0n0baca")

    res = main("karaca")
    print(res == "0c0r0kaca")


    res = main("burak")
    print(res == "k0r3baca")


    res = main("alpaca")
    print(res == "0c0pl0aca")
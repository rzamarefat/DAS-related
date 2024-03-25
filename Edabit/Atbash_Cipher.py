"""
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
Notes
Capitalisation should be retained.
Non-alphabetic characters should not be altered.
"""

def main(string):
    encoded_string = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encoded_string += chr(90 - (ord(char) - 65))
            else:
                encoded_string += chr(122 - (ord(char) - 97))
        else:
            encoded_string += char
            
    return encoded_string

if __name__ == "__main__":
    res = main("apple")
    print(res == "zkkov")
    res = main("Hello world!")
    print(res == "Svool dliow!")
    res = main("Christmas is the 25th of December")
    print(res == "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi")
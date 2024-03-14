"""
Create a function to test if a string is a valid pin or not.

A valid pin has:

Exactly 4 or 6 characters.
Only numerical characters (0-9).
No whitespace.
Examples
valid("1234") ➞ True

valid("45135") ➞ False

valid("89abc1") ➞ False

valid("900876") ➞ True

valid(" 4983") ➞ False
"""

def main(pin):
    
    if not(len(pin) in [4, 6]):
        return False
    
    for p in pin:
        if not(p.isdigit()) or p == " ":
            return False

    return True


if __name__ == "__main__":
    res = main("1234")
    print(res)
    res = main("45135")
    print(res)
    res = main("89abc1")
    print(res)
    res = main("900876")
    print(res)
    res = main(" 4983")
    print(res)
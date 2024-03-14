"""
Write a function that changes every letter to the next letter:

"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...

move("hello") ➞ "ifmmp"

move("bye") ➞ "czf"

move("welcome") ➞ "xfmdpnf"

"""

def main(word):
    result = ""
    for char in word:
        result += chr(ord(char)+1)

    return result

if __name__ == "__main__":
    res = main("hello")
    print(res)

    res = main("bye")
    print(res)

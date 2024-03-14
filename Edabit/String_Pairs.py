"""
Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.

See the below examples for a better understanding:

Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]

string_pairs("edabit") ➞ ["ed", "ab", "it"]

string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
"""



def main(string):
    if len(string)  % 2 != 0:
        string += "*"
    res = []
    for b in range(len(string) // 2):
        res.append(string[b * 2: (b+1)*2])

    return res


if __name__ == "__main__":
    res = main("mubashir")
    print(res)
    res = main("edabit")
    print(res)
    res = main("airforces")
    print(res)
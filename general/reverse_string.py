"""
the sky is blue -> blue is sky the
"""

def reverse_string(string):
    words = [w.strip() for w in string.split(" ")]

    return " ".join(words[::-1])

if __name__ == "__main__":
    res = reverse_string("the sky is blue")
    print(res)
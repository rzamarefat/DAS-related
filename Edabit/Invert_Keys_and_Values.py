"""
Write a function that inverts the keys and values of a dictionary.

Examples
invert({ "z": "q", "w": "f" })
➞ { "q": "z", "f": "w" }

invert({ "a": 1, "b": 2, "c": 3 })
➞ { 1: "a", 2: "b", 3: "c" }

invert({ "zebra": "koala", "horse": "camel" })
➞ { "koala": "zebra", "camel": "horse" }
"""
def main(dict_):
    reversed_dict = {} 

    for k,v in dict_.items():
        reversed_dict[v] = k

    return reversed_dict



if __name__ == "__main__":
    res = main({ "z": "q", "w": "f" })
    print(res)

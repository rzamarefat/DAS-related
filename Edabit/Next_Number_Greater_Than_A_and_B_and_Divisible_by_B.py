"""
You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.

Examples
divisible_by_b(17, 8) ➞ 24

divisible_by_b(98, 3) ➞ 99

divisible_by_b(14, 11) ➞ 22

"""


def main(a, b):
    num = max(a, b)
    while True:
        if num % b == 0:
            return num
        else:
            num += 1


if __name__ == "__main__":
    res = main(17, 8)
    print(res)
    res = main(98, 3)
    print(res)
    res = main(14, 11)
    print(res)
"""
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True
"""

def main(num):
    sum_ = 0
    for index, digit in enumerate(str(num)):
        digit = int(digit)

        sum_ += pow(digit, index+1)

    if sum_ == num:
        return True
    else:
        return False

if __name__ == "__main__":
    res = main(75)
    print(res)
    res = main(135)
    print(res)
    res = main(544)
    print(res)
    res = main(518)
    print(res)
    res = main(466)
    print(res)
    res = main(8)
    print(res)

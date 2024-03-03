"""
Write a Python program to swap two variables without temp variable.
"""

def swap_two_vars_no_temp(n1, n2):
    n1, n2 = n2, n1

    return n1, n2

if __name__ == "__main__":
    res = swap_two_vars_no_temp(1, 2)
    print(res)

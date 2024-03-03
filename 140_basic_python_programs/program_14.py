"""
Write a Python Program to Check Prime Number.
"""

def check_if_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    res = check_if_prime(2)

    print(res)
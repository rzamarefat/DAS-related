"""
Given a positive number x:

p = (p1, p2, …)
# Set of *prime* factors of x
If the square of every item in p is also a factor of x, then x is said to be a powerful number.

Create a function that takes a number and returns True if it's powerful, False if it's not.

Examples
is_powerful(36) ➞ True
# p = (2, 3) (prime factors of 36)
# 2^2 = 4 (factor of 36)
# 3^2 = 9 (factor of 36)

is_powerful(27) ➞ True

is_powerful(674) ➞ False
"""

def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors
    

def main(num):
    prime_factors_set = set(get_prime_factors(num))
    for prime in prime_factors_set:
        if num % (prime ** 2) != 0:
            return False
    return True


if __name__ == "__main__":
    res = main(36)
    print(res)
    res = main(27)
    print(res)
    res = main(674)
    print(res)
    

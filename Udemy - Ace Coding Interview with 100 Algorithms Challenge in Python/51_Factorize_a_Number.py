def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

if __name__ == "__main__":
    number = 36
    res = prime_factors(number)

    print(res)

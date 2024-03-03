def max_multiple(divisor, bound):
    return (bound) - bound % divisor


if __name__ == "__main__":
    res = max_multiple(divisor=4, bound=19)
    print(res)
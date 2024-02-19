def find_factorial(num):
    res = 1
    for i in range(1, num+1):
        res *= i

    return res

if __name__ == "__main__":
    res = find_factorial(4)
    print(res)


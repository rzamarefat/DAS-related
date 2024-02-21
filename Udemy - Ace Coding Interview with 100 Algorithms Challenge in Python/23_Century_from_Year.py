def find_century(year):
    if year <= 0:
        print("Invalid year")

    century = (year // 100) + 1

    return century

if __name__ == "__main__":
    res = find_century(2024)

    print(res)
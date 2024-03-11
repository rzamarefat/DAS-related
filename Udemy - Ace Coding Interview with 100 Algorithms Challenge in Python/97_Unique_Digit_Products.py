def find_unique_digit_products(number):
    unique_products = set()

    for i in range(1, number+1):
        product = 1
        for digit in str(i):
            product *= int(digit)
        
        unique_products.add(product)

    return len(unique_products)


if __name__ == "__main__":
    res = find_unique_digit_products(20)
    print(res)
def convert_decimal_to_binary(num):
    remained_holder = []
    while True:
        remained_holder.append(str(int(num % 2)))
        num /= 2

        if num < 2:
            remained_holder.append(str(int(num)))
            break

    
    return "".join(remained_holder)


if __name__ == "__main__":
    num = 45
    res = convert_decimal_to_binary(num)

    print(res)
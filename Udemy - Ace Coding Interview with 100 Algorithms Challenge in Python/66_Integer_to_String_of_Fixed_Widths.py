def integer_to_string_of_fixed_width(int_num, width):
    
    if width < len(str(int_num)):
        raise RuntimeError("Provide a width bigger than the number of digits")
    elif width == len(str(int_num)):
        return str(int_num)
    else:
        return "".join(["0" for digit in range(width - len(str(int_num)))]) + str(int_num)
    


if __name__ == "__main__":
    res = integer_to_string_of_fixed_width(int_num=456, width=10)
    print(res)
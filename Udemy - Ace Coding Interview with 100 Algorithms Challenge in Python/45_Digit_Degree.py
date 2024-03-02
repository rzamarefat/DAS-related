def find_digit_degree(number):
    data_holder = []
    degree = 0
    while True:
        sum_ = 0
        for char in str(number):
            sum_ += int(char)
        
        number = sum_

        degree += 1

        if len(str(number)) == 1:
            break
            
        

    return degree



        


if __name__ == "__main__":
    res = find_digit_degree(9875)
    print(res)
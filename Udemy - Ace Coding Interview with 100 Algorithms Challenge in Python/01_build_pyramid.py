def build_pyramid(rows_num):
    for i in range(rows_num):
        print(" " * (rows_num - i - 1), end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print(" ")
if __name__ == "__main__":
    build_pyramid(5)

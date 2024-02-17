def main(arr):
    max_element = float("-inf")
    for index, a in enumerate(arr):
        if not(index + 1 == len(arr)):
            product = a * arr[index + 1]
            if max_element < product:
                max_element = product
            
            
    return max_element



if __name__ == "__main__":
    arr = [2,5,3,4,6,7]
    res = main(arr)

    print(res)
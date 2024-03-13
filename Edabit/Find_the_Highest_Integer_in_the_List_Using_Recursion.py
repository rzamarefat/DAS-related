"""
Create a function that finds the highest integer in the list using recursion.
"""


def find_the_highest(array): 
    if len(array) == 1:
        return array[0]
    
    max_rest = find_the_highest(array[1:])
    if max_rest < array[0]:
        return array[0]
    else:
        return max_rest



if __name__ == "__main__":
    res = find_the_highest([-1, 3, 5, 6, 99, 12, 2])

    print(res)
"""
Write a Python program to swap two variables.
"""


def swap(variable1, variable2):
    temp = variable2

    variable2 = variable1
    variable1 = temp

    return variable1, variable2
    


if __name__ == "__main__":
    variable1, variable2 = 3, 10
    res=swap(variable1, variable2)

    print(res)

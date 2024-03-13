"""
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
"""


def sum_of_odd_and_even_numbers(array):
    sum_of_odd_nums = 0
    sum_of_even_nums = 0


    for a in array:
        if a % 2 ==0:
            sum_of_even_nums += a
        else:
            sum_of_odd_nums += a
    
    return sum_of_even_nums, sum_of_odd_nums


if __name__ == "__main__":
    sum_of_even_nums, sum_of_odd_nums = sum_of_odd_and_even_numbers([1, 2, 3, 4, 5, 6])

    print("sum_of_even_nums", sum_of_even_nums, "sum_of_odd_nums", sum_of_odd_nums)
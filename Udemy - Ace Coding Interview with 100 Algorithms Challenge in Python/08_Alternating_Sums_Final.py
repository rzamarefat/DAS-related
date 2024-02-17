def alternating_sum(nums):
    sum_odd = 0
    sum_even = 0
    for n in nums:
        if n % 2 == 0:
            sum_even += n
        else:
            sum_odd += n

    return sum_odd, sum_even



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    sum_odd, sum_even = alternating_sum(nums)

    print("sum_odd", sum_odd, "sum_even", sum_even)
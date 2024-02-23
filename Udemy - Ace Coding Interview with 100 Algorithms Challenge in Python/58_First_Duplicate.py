def find_first_duplicate(nums):
    checked_before = []
    for n in nums:
        if not(n in checked_before):
            checked_before.append(n)
        else:
            return n
    
    return "No duplicates"

if __name__ == "__main__":
    res = find_first_duplicate([5,6,4,8,5,6,1])
    res = find_first_duplicate([1,2,3,4,5,6,7])
    print(res)
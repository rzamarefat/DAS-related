"""
Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

Everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1],
[2, 4, 4, 3, 2, 2],
[5, 5, 5, 5, 4, 4],
[6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.
Not everyone can see the front-stage in the example below:

# FRONT STAGE
[[1, 2, 3, 2, 1, 1], 
[2, 4, 4, 3, 2, 2], 
[5, 5, 5, 10, 4, 4], 
[6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
The function should return True if every number can see the front-stage, and False if even a single number cannot.
"""

def main(seats):
    for col_index in range(len(seats[0])):
        for row_index in range(len(seats)):
            if row_index+1 < len(seats):
                if seats[row_index][col_index] > seats[row_index + 1][col_index]:
                    return False
            
    return True

        



if __name__ == "__main__":
    seats=[[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 2, 2],
            [5, 5, 5, 5, 4, 4],
            [6, 6, 7, 6, 5, 5]]
    res = main(seats)

    print(res == True)

    seats = [[1, 2, 3, 2, 1, 1], 
            [2, 4, 4, 3, 2, 2], 
            [5, 5, 5, 10, 4, 4], 
            [6, 6, 7, 6, 5, 5]]
    
    res = main(seats)
    print(res == False)


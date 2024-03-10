def find_crossing_sum_of_a_matrix(matrix, target_row, target_col):
    horzontal_sum = sum(matrix[target_row])
    vertical_sum = sum([row[target_col] for row in matrix])

    return horzontal_sum + vertical_sum - matrix[target_row][target_col] 



if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    target_row = 1
    target_col = 1

    res = find_crossing_sum_of_a_matrix(matrix, target_row, target_col) 
    print(res)
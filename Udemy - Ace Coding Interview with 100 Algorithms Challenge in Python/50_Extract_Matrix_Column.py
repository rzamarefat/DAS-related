def extract_matrix_column(matrix, which_column):
    if which_column > len(matrix[0]):
        raise ValueError()

    target_col = []
    for row in matrix:
        target_col.append(row[which_column])

    return target_col


if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    
    which_column = 2
    res = extract_matrix_column(matrix, which_column)
    print(res)
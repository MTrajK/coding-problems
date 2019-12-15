'''
Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

=========================================
Use first column and first row for marking when 0 is found.
    Time Complexity:    O(N*M)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def set_matrix_zeroes(matrix):
    n = len(matrix)
    if n == 0:
        return
    m = len(matrix[0])

    # check if 0 exist in first row
    is_row = False
    for j in range(m):
        if matrix[0][j] == 0:
            is_row = True
    # check if 0 exist in first column
    is_col = False
    for i in range(n):
        if matrix[i][0] == 0:
            is_col = True

    # find which columns and rows should be 0
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    # set 0 if the row or column where this element is located is 0
    for i in range(1, n):
        for j in range(1, m):
            if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                matrix[i][j] = 0

    # fill the first row with 0 if needed
    if is_row:
        for j in range(m):
            matrix[0][j] = 0
    # fill the first column with 0 if needed
    if is_col:
        for i in range(n):
            matrix[i][0] = 0


###########
# Testing #
###########

# Test 1
# Correct result => [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
set_matrix_zeroes(mat)
print(mat)

# Test 2
# Correct result => [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_matrix_zeroes(mat)
print(mat)
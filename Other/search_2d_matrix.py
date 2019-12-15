'''
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Input: target = 21
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Output: True

=========================================
Start from bottom left corner and search in top right direction.
    Time Complexity:    O(N + M)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def search_2d_matrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])

    j = 0
    i = n - 1

    while (i >= 0) and (j < m):
        if matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
        else:
            return True

    return False


###########
# Testing #
###########

# Test 1
# Correct result => True
print(search_2d_matrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 21))

# Test 2
# Correct result => False
print(search_2d_matrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
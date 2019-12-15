'''
Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

=========================================
Simulate spiral moving, start from (0,0) and when a border is reached change the X or Y direction.
    Time Complexity:    O(N*M)
    Space Complexity:   O(N*M)
'''


############
# Solution #
############

def spiral_matrix(matrix):
    n = len(matrix)
    if n == 0:
        return []

    m = len(matrix[0])
    if m == 0:
        return []

    total = n * m
    res = []

    n -= 1
    xDir, yDir = 1, 1
    x, y = 0, -1

    while len(res) < total:
        for i in range(m):
            y += yDir
            res.append(matrix[x][y])
        m -= 1 # decrease horizontal moving steps
        yDir *= -1 # change the Y direction

        for i in range(n):
            x += xDir
            res.append(matrix[x][y])
        n -= 1 # decrease vertical moving steps
        xDir *= -1 # change the Y direction

    return res


###########
# Testing #
###########

# Test 1
# Correct result => [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiral_matrix([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]))

# Test 2
# Correct result => [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(spiral_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
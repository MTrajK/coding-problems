'''
River Sizes

You are given a two-dimensional array (matrix) of potentially unequal height and width containing only 0s and 1s.
Each 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are
either horizontally or vertically adjacent (but not diagonally adjacent).
The number of adjacent 1s forming a river determine its size.
Write a function that returns an array of the sizes of all rivers represented in the input matrix.
Note that these sizes do not need to be in any particular order.

Input:
[
[1, 0, 0, 1],
[1, 0, 1, 0],
[0, 0, 1, 0],
[1, 0, 1, 0]
]
Output: [2, 1, 3, 1]

=========================================
This problem can be solved using DFS or BFS.
If 1 is found, find all horizontal or vertical neighbours (1s), and mark them as 0.
    Time Complexity:    O(N*M)
    Space Complexity:   O(N*M)     , because of recursion calls stack
'''


############
# Solution #
############

def river_sizes(matrix):
    n = len(matrix)
    m = len(matrix[0])

    results = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                # find the river size
                size = dfs((i, j), matrix)

                # save the river size
                results.append(size)

    return results

def dfs(coord, matrix):
    (i, j) = coord

    if i < 0 or j < 0:
        # invalid position
        return 0

    n = len(matrix)
    m = len(matrix[0])

    if i == n or j == m:
        # invalid position
        return 0

    if matrix[i][j] == 0:
        # not a river
        return 0

    # update the matrix, the matrix is passed by reference
    matrix[i][j] = 0
    # this position is part of river
    size = 1

    # directions: down, left, up, right
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # check all 4 directions
    for d in dirs:
        size += dfs((i + d[0], j + d[1]), matrix)

    return size


###########
# Testing #
###########

# Test 1
# Correct result => [2, 1, 3, 1]
matrix = [
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0]
    ]
print(river_sizes(matrix))
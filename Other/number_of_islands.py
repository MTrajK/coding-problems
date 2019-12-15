'''
Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input:  [
            ['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']
        ]
Output: 1

Input:  [
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
        ]
Output: 3

=========================================
This problem can be solved in several ways (using DFS recursion or using the stack data structure) i'll solve it with BFS using Queue data structure.
    Time Complexity:    O(M * N)
    Space Complexity:   O(M * N)
'''


############
# Solution #
############

from collections import deque

def num_of_islands(grid):
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])

    islands = 0
    queue = deque()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            # search for an island
            if grid[i][j] == '1':
                islands += 1
                queue.append((i, j))

                # BFS
                while queue:
                    coord = queue.popleft()
                    x, y = coord
                    
                    if grid[x][y] != '1':
                        continue
                    # delete the island
                    grid[x][y] = '0'

                    for direction in directions:
                        # calculate the next position
                        next_x, next_y = (x + direction[0], y + direction[1])
                        # check if the next position is valid
                        if (next_x < 0) or (next_x >= n):
                            continue
                        if (next_y < 0) or (next_y >= m):
                            continue
                        # save this position
                        queue.append((next_x, next_y))

    return islands


###########
# Testing #
###########

# Test 1
# Correct result => 3
print(num_of_islands([['1','1','0','0','0'], ['1','1','0','0','0'], ['0','0','1','0','0'], ['0','0','0','1', '1']]))
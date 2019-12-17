'''
Find min path

You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up, left, down, and right.
You cannot move through walls. You cannot wrap around the edges of the board.

Input:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
start = (3, 0)
end = (0, 0)
Output: 7
Output explanation: Starting bottom left and ending top left,
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

=========================================
BFS solution using queue.
    Time Complexity:    O(N * M)
    Space Complexity:   O(N * M)
'''


############
# Solution #
############

from collections import deque

def find_min_path(board, start, end):
    n = len(board)
    m = len(board[0])

    # create a visited array
    visited = [[False for el in range(m)] for row in range(n)]

    queue = deque()
    queue.append((start, 0))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # up, right, down, left

    # simple bfs
    while queue:
        el = queue.popleft()
        position = el[0]
        steps = el[1]

        # check if this position is already visited
        if visited[position[0]][position[1]]:
            continue

        visited[position[0]][position[1]] = True

        # check if this position is walkable
        if board[position[0]][position[1]] == 't':
            continue

        # if the end was reached return steps
        if position == end:
            return steps

        newSteps = steps + 1

        # add all neighbours at the end of the queue
        for d in directions:
            x = position[0] + d[0]
            y = position[1] + d[1]

            if (x < n) and (x >= 0) and (y < m) and (y >= 0):
                queue.append(((x, y), newSteps))

    # the path was not found
    return None


###########
# Testing #
###########

# Test 1
# Correct result => 7
f = 'f'
t = 't'
print(find_min_path([[f, f, f, f], [t, t, f, t], [f, f, f, f], [f, f, f, f]], (3, 0), (0, 0)))
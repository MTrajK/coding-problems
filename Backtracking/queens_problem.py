'''
Queens Problem

You have an N by N board. Write a function that, given N, returns the number of possible arrangements
of the board where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.

=========================================
Backtracking solution.
    Time Complexity:    O(N!) (but I think it's much faster!)
    Space Complexity:   O(N)
* There are much faster solutions, like O(N^2)
'''


############
# Solution #
############

def place_n_queens(n):
    columns = [False for i in range(n)]
    order = []

    return backtracking(columns, order)

def backtracking(columns, order):
    # columns and order are references, no extra memory for those arrays (they are just pointers)
    n = len(columns)

    if len(order) == n:
        return 1

    total = 0

    for i in range(n):
        if (not columns[i]) and check_diagonals(order, i):
            order.append(i)
            columns[i] = True
            total += backtracking(columns, order)
            # return to the old state
            columns[i] = False
            del order[-1]

    return total

def check_diagonals(order, pos):
    current_row = len(order)

    for i in range(current_row):
        if (i - order[i]) == (current_row - pos):
            return False
        if (i + order[i]) == (current_row + pos):
            return False

    return True


###########
# Testing #
###########

# Test 1
# Correct result => 1
print(place_n_queens(1))

# Test 2
# Correct result => 0
print(place_n_queens(2))

# Test 3
# Correct result => 0
print(place_n_queens(3))

# Test 4
# Correct result => 2
print(place_n_queens(4))

# Test 5
# Correct result => 10
print(place_n_queens(5))

# Test 6
# Correct result => 4
print(place_n_queens(6))

# Test 7
# Correct result => 40
print(place_n_queens(7))

# Test 8
# Correct result => 92
print(place_n_queens(8))

# Test 9
# Correct result => 352
print(place_n_queens(9))

# Test 10
# Correct result => 724
print(place_n_queens(10))
'''
Unique Paths

Find the unique paths in a matrix starting from the upper left corner and ending in the bottom right corner.

=========================================
Dynamic programming (looking from the left and up neighbour), but this is a slower solution, see the next one.
    Time Complexity:    O(N*M)
    Space Complexity:   O(N*M)
The DP table is creating an Pascal Triangle, so this problem can be easily solved by using the combinatorial formula!
Much faster and doesn't use extra space.
    Time Complexity:    O(min(M, N))
    Space Complexity:   O(1)
'''

################################
# Solution Dynamic Programming #
################################

def unique_paths_dp(n, m):
    # all values at i=0 should be 1 (the rest are not important, they'll be computed later)
    dp = [[1 for j in range(m)] for i in range(n)]

    # calculate only inner values
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[n-1][m-1]


#################################
# Solution Combinations Formula #
#################################

def unique_paths(n, m):
    m, n = min(m, n), max(m, n)
    lvl = m + n - 2
    pos = m - 1
    comb = 1

    # combinations formula C(N, R) = N! / R! * (N - R)!
    for i in range(1, pos + 1):
        comb *= lvl
        comb /= i
        lvl -= 1

    return int(comb + 0.001) # 0.001 just in case, because of overflow


###########
# Testing #
###########

# Test 1
# Correct result => 924
n, m = 7, 7
print(unique_paths(n, m))
print(unique_paths_dp(n, m))

# Test 2
# Correct result => 28
n, m = 7, 3
print(unique_paths(n, m))
print(unique_paths_dp(n, m))

# Test 3
# Correct result => 28
n, m = 3, 7
print(unique_paths(n, m))
print(unique_paths_dp(n, m))
'''
Climbing Staircase 

There exists a staircase with N steps, and you can climb up either X different steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

Input: steps = [1, 2], height = 4
Output: 5
Output explanation:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

=========================================
Dynamic Programing
    Time Complexity:    O(N*S)
    Space Complexity:   O(N)
If steps are only [1, 2], this problem can be solved using Fibonacci algorithm, because ways(n) = ways(n-1) + ways(n-2).
    Time Complexity:    O(Fib(N))
    Space Complexity:   O(1)
'''


############
# Solution #
############

def climbing_staircase(steps, height):
    dp = [0 for i in range(height)]

    # add all steps into dp
    for s in steps:
        if s <= height:
            dp[s - 1] = 1

    # for each current position look how you can arrive there
    for i in range(height):
        for s in steps:
            if i - s >= 0:
                dp[i] += dp[i - s]

    return dp[height - 1]


###########
# Testing #
###########

# Test 1
# Correct result => 5
print(climbing_staircase([1, 2], 4))

# Test 2
# Correct result => 3
print(climbing_staircase([1, 3, 5], 4))
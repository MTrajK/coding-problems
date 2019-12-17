'''
Interleaving Strings

Given are three strings A, B and C.
C is said to be interleaving of A and B, if:
- it contains all characters of A and B, and
- order of all characters from A and B is preserved in C
Your task is to count in how many ways C can be formed by interleaving of A and B.

Input: A='xy', B= 'xz', C: 'xxyz'
Output: 2
Output explanation: 
    1) Take 'x' from A, then 'x' from B, then 'y' from A and at the end 'z' from B.
    2) Take 'x' from B, then 'x' from A, then 'y' from A and at the end 'z' from B.

=========================================
2D Dynamic programming solution.
    Time Complexity:    O(N*M)
    Space Complexity:   O(N*M)
1D Dynamic programming solution. Only the last two rows from the whole matrix are used, but that could be represented using only 1 row.
    Time Complexity:    O(N*M)
    Space Complexity:   O(M)
'''

##############
# Solution 1 #
##############

def interleaving_strings_1(A, B, C):
    nA, nB, nC = len(A), len(B), len(C)
    if nA + nB != nC:
        return 0
    
    dp = [[0 for j in range(nB + 1)] for i in range(nA + 1)]

    # starting values
    dp[0][0] = 1

    for i in range(1, nA + 1):
        if A[i - 1] == C[i - 1]:
            # short form of if A[i - 1] == C[i - 1] and dp[i - 1][0] == 1
            # dp[i][0] and dp[0][1] can be only 0 or 1
            dp[i][0] = dp[i - 1][0]

    for i in range(1, nB + 1):
        if B[i - 1] == C[i - 1]:
            dp[0][i] = dp[0][i - 1]
    
    # run dp
    for i in range(1, nA + 1):
        for j in range(1, nB + 1):
            if A[i - 1] == C[i + j - 1]:
                # look for the dp value from the previous position
                dp[i][j] += dp[i - 1][j]
            if B[j - 1] == C[i + j - 1]:
                # look for the dp value from the previous position
                dp[i][j] += dp[i][j - 1]

    return dp[nA][nB]


##############
# Solution 2 #
##############

def interleaving_strings_2(A, B, C):
    nA, nB, nC = len(A), len(B), len(C)
    if nA + nB != nC:
        return 0
    
    dp = [0 for j in range(nB + 1)]

    # starting values
    dp[0] = 1

    for i in range(1, nB + 1):
        if B[i - 1] == C[i - 1]:
            dp[i] = dp[i - 1]
    
    # run dp
    for i in range(1, nA + 1):
        if A[i - 1] != C[i - 1]:
            # reset the value
            dp[0] = 0

        for j in range(1, nB + 1):
            if A[i - 1] != C[i + j - 1]:
                # reset the value
                dp[j] = 0
            if B[j - 1] == C[i + j - 1]:
                dp[j] += dp[j - 1]

    return dp[nB]


###########
# Testing #
###########

# Test 1
# Correct result => 2
a, b, c = 'xy', 'xz', 'xxyz'
print(interleaving_strings_1(a, b, c))
print(interleaving_strings_2(a, b, c))
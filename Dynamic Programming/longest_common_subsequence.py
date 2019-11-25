'''
Longest Common Subsequence

Given 2 strings, find the longest common subseqence - https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
NOT Longest Common Substring, this is a different problem.
Substring is a string composed ONLY of neighboring chars, subsequence could contain non-neighboring chars.

Input: 'ABAZDC', 'BACBAD'
Output: 'ABAD'

Input: 'I'm meto', 'I am Meto'
Output: 'Im eto'

=========================================
Dynamic programming solution.
Find more details here: https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    Time Complexity:    O(N * M)
    Space Complexity:   O(N * M)    , can be O(M) see longest_common_substring.py solution (but you'll need to save subsequences)
'''


############
# Solution #
############

def longest_common_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    # create dp matrix
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # run dp
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # checks only in 3 directions in the table
            # in short: to the current position dp could come from those 3 previous positions
            #   ^  ^
            #    \ |
            #   <- O
            if str1[i - 1] == str2[j - 1]:
                # from this position dp could come only if there is a match in the previous chars
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # dp could come from these positions only if there is no much
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # find the subseqence/string
    letters = dp[n][m]
    # use an array for storing the chars because string manipulation operations are not time and space efficient
    result = ['' for i in range(letters)]
    i = n
    j = m

    while (i != 0) and (j != 0):
        # use the inverse logic from upper code (filling the dp table)
        if str1[i - 1] == str2[j - 1]:
            letters -= 1
            result[letters] = str1[i - 1]
            j -= 1
            i -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            j -= 1
        else:
            i -= 1

    return ''.join(result)


###########
# Testing #
###########

# Test 1
# Correct result => 'ABAD'
print(longest_common_subsequence('ABAZDC', 'BACBAD'))

# Test 2
# Correct result => 'Im eto'
print(longest_common_subsequence('I\'m meto', 'I am Meto'))

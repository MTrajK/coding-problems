'''
Longest Common Substring

Given two strings X and Y, find the of longest common substring.

Input: 'GeeksforGeeks', 'GeeksQuiz'
Output: 'Geeks'

=========================================
Dynamic Programming Solution.
    Time Complexity:    O(N * M)
    Space Complexity:   O(M)
* For this problem exists a faster solution, using Suffix tree, Time Complexity O(N + M).
'''


############
# Solution #
############

def longest_common_substring(str1, str2):
    n, m = len(str1), len(str2)
    # instead of creating a whole dp table, use only 2 rows (current and previous row)
    curr = [0 for j in range(m + 1)]
    prev = []
    max_length = 0
    max_idx = 0

    for i in range(1, n + 1):
        # save the previous row and create the current row
        prev = curr
        curr = [0 for j in range(m + 1)]

        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                # search only for matching chars
                curr[j] = prev[j - 1] + 1

                if curr[j] > max_length:
                    # save the last matching index of the first string
                    max_length = curr[j]
                    max_idx = i

    return str1[max_idx - max_length: max_idx]


###########
# Testing #
###########

# Test 1
# Correct result => BABC
print(longest_common_substring('ABABC', 'BABCA'))

# Test 2
# Correct result => Geeks
print(longest_common_substring('GeeksforGeeks', 'GeeksQuiz'))

# Test 3
# Correct result => abcd
print(longest_common_substring('abcdxyz', 'xyzabcd'))

# Test 4
# Correct result => abcdez
print(longest_common_substring('zxabcdezy', 'yzabcdezx'))
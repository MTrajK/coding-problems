'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''.

Input: ['flower', 'flow', 'flight']
Output: 'fl'

Input: ['dog', 'racecar', 'car']
Output: ''

Input: ['aa', 'a']
Output: 'a'

=========================================
Many solutions for this problem exist (Divide and Conquer, Trie, etc) but this is the simplest and the fastest one.
Use the first string as LCP and iterate the rest in each step compare it with another one.
    Time Complexity:    O(N*A)  , N = number of strings, A = average chars, or simplest notation O(S) = total number of chars
    Space Complexity:   O(1)
'''


############
# Solution #
############

def longest_common_prefix(strs):
    n = len(strs)
    if n == 0:
        return ''

    lcp = strs[0]
    # instead of string manipulations, manipulate with the last common index
    lcp_idx = len(lcp)

    for i in range(1, n):
        lcp_idx = min(lcp_idx, len(strs[i]))

        for j in range(lcp_idx):
            if lcp[j] != strs[i][j]:
                lcp_idx = j
                break

    return lcp[:lcp_idx]
    '''
    # if you like string manipulations, you can use this code
    # i don't like string manipulations in Python because they're immutable
    lcp = strs[0]
    for i in range(1, n):
        lcp = lcp[:len(strs[i])]
        for j in range(len(lcp)):
            if lcp[j] != strs[i][j]:
                lcp = lcp[:j]
                break
    return lcp
    '''


###########
# Testing #
###########

# Test 1
# Correct result => 'fl'
print(longest_common_prefix(['flower', 'flow', 'flight']))

# Test 2
# Correct result => ''
print(longest_common_prefix(['dog', 'racecar', 'car']))

# Test 3
# Correct result => 'a'
print(longest_common_prefix(['aa', 'a']))
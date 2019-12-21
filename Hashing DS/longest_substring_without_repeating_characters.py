'''
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Input: 'abcabcbb'
Output: 3
Output explanation: The answer is 'abc', with the length of 3.

Input: 'bbbbb'
Output: 1
Output explanation: The answer is 'b', with the length of 1.

=========================================
Simple string iteration, use hashset to save unique characters.
If the current character exists in the set then move the left index till the one
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def length_of_longest_substring(s):
    unique_chars = set()
    max_length = 0
    left = 0
    n = len(s)

    for i in range(n):
        while s[i] in unique_chars:
            # remove till the current char is unique
            unique_chars.remove(s[left])
            left += 1

        # in this moment you're sure that the current char is unique
        unique_chars.add(s[i])
        max_length = max(max_length, i - left + 1)

    return max_length


###########
# Testing #
###########

# Test 1
# Correct result => 3
print(length_of_longest_substring('abcabcbb'))

# Test 2
# Correct result => 1
print(length_of_longest_substring('bbbbb'))
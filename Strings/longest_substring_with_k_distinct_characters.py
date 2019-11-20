'''
Longest Substring With k Distinct Characters

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

Input: s = 'abcba', k = 2
Output: 'bcb'

=========================================
Simple solution (like sliding window or queue, add to the end and remove from the front).
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def longest_substring_with_distinct_characters(s, k):
    letters = {}
    longest = 0
    length = 0

    for i in range(len(s)):
        if s[i] in letters:
            # if this letter exists then only increase the counter and length
            letters[s[i]] += 1
            length += 1
        else:
            # if this letter doesn't exist then remove all distinct letters from the front
            # so the count of distinct letters will be k-1
            while len(letters) == k:
                firstLetter = s[i - length]
                letters[firstLetter] -= 1 # decrease the counter
                if letters[firstLetter] == 0:
                    # remove this letter from the dictionary because
                    # in the susbtring there are no letters like this
                    del letters[firstLetter]
                length -= 1

            # add the new letter in the dictionary
            letters[s[i]] = 1
            length += 1

        # check if this length is the longest one
        longest = max(longest, length)

    return longest


###########
# Testing #
###########

# Test 1
# Correct result => 3
print(longest_substring_with_distinct_characters('abcba', 2))

# Test 2
# Correct result => 8
print(longest_substring_with_distinct_characters('abcbcbcbba', 2))
'''
Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters is just like on the telephone buttons. Note that 1 does not map to any letters.

Input: '23'
Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

=========================================
This problem could be solved in several ways (using recursion, stack, queue...) and the complexity is same in all, but this one has the simplest code.
Iterate all digits and in each step look for the previous combinations, create a new 3 or 4 combinations from each combination using the mapping letters.
    Time Complexity:    O(3^N * 4^M)    , N = number of digits that maps to 3 letters, M = number of digits that maps to 4 letters
    Space Complexity:   O(3^N * 4^M)
'''


############
# Solution #
############

def letter_combinations(digits):
    if len(digits) == 0:
        return []

    mappings = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    prev_combinations = ['']

    for digit in digits:
        new_combinations = []
        for combination in prev_combinations:
            # use the mappings and create new combinations
            for mapping in mappings[digit]:
                new_combinations.append(combination + mapping)
        # save the newest combinations
        prev_combinations = new_combinations

    return prev_combinations


###########
# Testing #
###########

# Test 1
# Correct result => ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(letter_combinations('23'))
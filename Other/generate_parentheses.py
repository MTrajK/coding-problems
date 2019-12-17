'''
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: 3
Output:
        [
            '((()))',
            '(()())',
            '(())()',
            '()(())',
            '()()()'
        ]

=========================================
This problem could be solved in several ways (using stack, queue, or just a simple list - see letter_combinations.py), all of them have the same complexity.
I'll solve it using simple recursive algorithm.
    Time Complexity:    O(4^N)      , O(2^(2*N)) = O(4^N)
    Space Complexity:   O(4^N)
'''


############
# Solution #
############

def generate_parentheses(n):
    result = []
    if n == 0:
        return result

    combinations(result, n, n, '')

    return result


def combinations(result, open_left, close_left, combination):
    if close_left == 0:
        # a new combination is created (no more open or close parentheses)
        result.append(combination)
    elif open_left == 0:
        # no more open parentheses, so all left parentheses must be closed (just add the missing close parentheses)
        result.append(combination + (')' * close_left))
    else:
        combinations(result, open_left - 1, close_left, combination + '(')

        # check if there is a pair for this close parenthesis
        if open_left < close_left:
            combinations(result, open_left, close_left - 1, combination + ')')


###########
# Testing #
###########

# Test 1
# Correct result => ['((()))', '(()())', '(())()', '()(())', '()()()']
print(generate_parentheses(3))
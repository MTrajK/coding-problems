'''
Valid Parentheses

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string '([])[]({})', you should return true.
Given the string '([)]' or '((()', you should return false.

Input: '()[{([]{})}]'
Output: True

=========================================
Use stack. Add open brackets in the stack, remove the last bracket from the stack if there is a closing brackets.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

from collections import deque

def is_valid(string):
    closing = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = deque()

    for char in string:
        if char in closing:
            if len(stack) == 0:
                return False

            last = stack.pop()
            if last != closing[char]:
                return False
        else:
            stack.append(char)

    return True


###########
# Testing #
###########

# Test 1
# Correct result => True
print(is_valid('()[{([]{})}]'))

# Test 2
# Correct result => False
print(is_valid('()[{([]{]})}]'))

# Test 3
# Correct result => False
print(is_valid('(]]])'))
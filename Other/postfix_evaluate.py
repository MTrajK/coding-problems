'''
Postfix Evaluate

When arithmetic expressions are given in the familiar infix notation 2 + 3 * 4, we need to use
parentheses to force a different evaluation order than the usual PEMDAS order determined by
precedence and associativity. Writing arithmetic expressions in postfix notation (also known as
Reverse Polish Notation) may look strange to us humans accustomed to the conventional infix
notation, but is computationally much easier to handle, since postfix notation allows any evaluation
order to be expressed without using any parentheses at all! A postfix expression is given as a list of
items that can be either individual integers or one of the strings '+', '-', '*' and '/' for the four
possible arithmetic operators. Calculate the result of the postfix expression.

Input: [2, 3, '+', 4, '*']
Output: 20
Output explanation: (2+3) * 4

Input: [1, 2, 3, 4, 5, 6, '*', '*', '*', '*', '*']
Output: 720
Output explanation: 1 * 2 * 3 * 4 * 5 * 6

=========================================
Use stack, save all numbers into the stack.
When a sign comes, pop the last 2 numbers from the stack, calculate their result and return the result into the stack.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

from collections import deque

def postfix_evaluate(items):
    stack = deque()
    # lambda functions for all 4 operations
    operations = {
        '+': (lambda a, b: a + b),
        '-': (lambda a, b: a - b),
        '*': (lambda a, b: a * b),
        '/': (lambda a, b: 0 if (b == 0) else (a // b))
    }

    for item in items:
        # check if the item is a sign or a number
        if item in operations:
            b = stack.pop()
            a = stack.pop()

            result = operations[item](a, b)

            stack.append(result)
        else:
            stack.append(item)

    return stack.pop()


###########
# Testing #
###########

# Test 1
# Correct result => 20
print(postfix_evaluate([2, 3, '+', 4, '*']))

# Test 2
# Correct result => 14
print(postfix_evaluate([2, 3, 4, '*', '+']))

# Test 3
# Correct result => 0
print(postfix_evaluate([3, 3, 3, '-', '/']))

# Test 4
# Correct result => 2
print(postfix_evaluate([7, 3, '/']))

# Test 5
# Correct result => 720
print(postfix_evaluate([1, 2, 3, 4, 5, 6, '*', '*', '*', '*', '*']))
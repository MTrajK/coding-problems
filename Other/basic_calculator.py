'''
Basic Calculator

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open '(' and closing parentheses ')',
the plus '+' or minus sign '-', non-negative integers and empty spaces ' '.

Input: '(1+(4+5+2)-3)+(6+8)'
Output: 23

Input: ' 2-1 + 2 '
Output: 3

=========================================
Start from the first character and respect the math rules. When brackets come, go inside the brackets
and compute the inner result, after that continue with adding or subtracting.
    Time Complexity:    O(N)
    Space Complexity:   O(K)    , much less than N (the deepest level of brackets)
'''


############
# Solution #
############

def basic_calculator(s):
    return calculate(s, 0)[0]

def calculate(s, i):
    sign = 1    # 1 means '+' and -1 means '-'
    res = 0
    num = 0

    while i < len(s) and s[i] != ')':
        if s[i] >= '0' and s[i] <= '9':
            # find the whole number
            num = num * 10 + int(s[i])
        elif s[i] == '(':
            # calculate inside the brackets
            brackets = calculate(s, i + 1)
            res += brackets[0] * sign
            i = brackets[1] # continue from the new i
        elif s[i] != ' ':
            # add the previous number using the old sign
            res += num * sign
            num = 0

            if s[i] == '-':
                sign = -1
            elif s[i] == '+':
                sign = 1

        i += 1

    res += num * sign
    return (res, i)


###########
# Testing #
###########

# Test 1
# Correct result => 23
print(basic_calculator('(1+(4+5+2)-3)+(6+8)'))

# Test 2
# Correct result => 3
print(basic_calculator(' 2-1 + 2 '))
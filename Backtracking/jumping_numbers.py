'''
Jumping numbers

A number is called as a Jumping Number if all adjacent digits in it differ by 1.
The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers.
For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Input: 20
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

=========================================
Make a tree (DFS way/backtracking), for each next digit take the last digit, go up and down
(example: 123, last digit is 3, so next digit should be 2 or 4).
    Time Complexity:    O(9 * 2^(NumOfDigits(N) - 1))
    Space Complexity:   O(1)        , recursion stack will have depth 9 (but this can be considered as constant)
'''


############
# Solution #
############

def jumping_numbers(x):
    result = []

    # take all 9 possible starting combinations
    for i in range(1, 10):
        jumping_num(i, x, result)

    return result

def jumping_num(num, x, result):
    if num > x:
        return

    result.append(num)

    last_digit = num % 10
    next_num = num * 10

    # decrease the last digit by one
    if last_digit != 0:
        jumping_num(next_num + last_digit - 1, x, result)

    # increase the last digit by one
    if last_digit != 9:
        jumping_num(next_num + last_digit + 1, x, result)


###########
# Testing #
###########

# Test 1
# Correct result => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
print(jumping_numbers(20))

# Test 2
# Correct result => [1, 10, 12, 2, 21, 23, 3, 32, 34, 4, 43, 45, 5, 54, 56, 6, 65, 67, 7, 76, 78, 8, 87, 89, 9, 98]
print(jumping_numbers(100))
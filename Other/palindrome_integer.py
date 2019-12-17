'''
Palindrome Integer

Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Input: 121
Output: True

Input: -121
Output: False
Output explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: 10
Output: false
Output oxplanation: Reads 01 from right to left. Therefore it is not a palindrome.

=========================================
Juste reverse the number and compare it with the original.
    Time Complexity:    O(N)    , N = number of digits
    Space Complexity:   O(1)
If you care about integer overflow (in Python you shouldn't care about this), then reverse only a half of the number
and compare it with the other half. Also this solution is faster than the previous one because iterates only a half of the number.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def palindrome_integer_1(x):
    if x < 0:
        return False

    rev = 0
    temp = x
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10

    return rev == x


##############
# Solution 2 #
##############

def palindrome_integer_2(x):
    # check if negative or ends with zero
    if (x < 0) or (x > 0 and x % 10 == 0):
        return False

    rev = 0
    # if the reversed number is bigger from the original
    # that means the reversed number has same number of digits or more (1 or 2 more)
    while x > rev:
        rev = (rev * 10) + (x % 10)
        x //= 10

    # first comparison is for even number of digits and the second for odd number of digits
    return (rev == x) or (rev // 10 == x)


###########
# Testing #
###########

# Test 1
# Correct result => True
x = 121
print(palindrome_integer_1(x))
print(palindrome_integer_2(x))

# Test 2
# Correct result => False
x = -121
print(palindrome_integer_1(x))
print(palindrome_integer_2(x))

# Test 2
# Correct result => False
x = 10
print(palindrome_integer_1(x))
print(palindrome_integer_2(x))
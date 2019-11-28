'''
Find Nth Fibonacci Number

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
Given a number n, print n-th Fibonacci Number.

Input: 8
Output: 34

=========================================
Many solutions for this problem exist, I'll show 6 different solutions,
starting from the worst to the best.

The simplest recursive solution.
    Time Complexity:    O(2^N)  , actually ~1.6^N, the golden ratio
    Space Complexity:   O(N)    , because of the recursion stack
Recursion with memoizing. Much faster, 2^N-N less operations.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
Dynamic programming.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
Space optimized dynamic programming. (don't need a whole array, only 2 variables are needed)
    Time Complexity:    O(N)
    Space Complexity:   O(1)
Matrix power.
start matrix:   | 1  1 |
                | 1  0 |

result matrix:  | Fn+1  Fn   |
                | Fn    Fn-1 |

result * start =    | Fn+1 * 1 + Fn * 1    Fn+1 * 1 + Fn * 0 |
                    | Fn * 1 + Fn-1 * 1    Fn * 1 + Fn-1 * 0 |

               =    | Fn+1 + Fn    Fn+1 |
                    | Fn + Fn-1    Fn   |

               =    | Fn+1 + Fn    Fn+1 |
                    | Fn+1         Fn   |
    Time Complexity:    O(N)
    Space Complexity:   O(1)
Time optimized matrix power. (using recursive divide and conquer approach)
    Time Complexity:    O(LogN)
    Space Complexity:   O(LogN)     , because of the recursion stack
Time and space optimized matrix multiplication. (without recursion, just looping)
    Time Complexity:    O(LogN)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def fibonacci_1(n):
    if (n == 0) or (n == 1):
        return n

    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


##############
# Solution 2 #
##############

# hashmap
fib = {0: 0, 1: 1}

def fibonacci_2(n):
    if n in fib:
        return fib[n]

    fib[n] = fibonacci_2(n - 1) + fibonacci_2(n - 2)

    return fib[n]


##############
# Solution 3 #
##############

def fibonacci_3(n):
    dp = [0 for i in range(max(2, n + 1))]
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


##############
# Solution 4 #
##############

def fibonacci_4(n):
    dp0, dp1 = 0, 1

    for i in range(n):
        dp0, dp1 = dp1, dp0 + dp1

    return dp0


#################################
# Helper for the next solutions #
#################################

def matrix_mult(a, b):
    ''' a = a * b
    Matrices (2x2 matrix) Multiplication method used for the next solutions.
    The result of multiplication is saved in 'a' (because of that, the reference
    shouldn't be changed, only change the values after all computations are completed
    because 'b' could be the same reference/matrix as 'a').
    '''
    a00 = a[0][0]*b[0][0] + a[0][1]*b[1][0]
    a01 = a[0][0]*b[0][1] + a[0][1]*b[1][1]
    a10 = a[1][0]*b[0][0] + a[1][1]*b[1][0]
    a11 = a[1][0]*b[0][1] + a[1][1]*b[1][1]
    a[0][0] = a00
    a[0][1] = a01
    a[1][0] = a10
    a[1][1] = a11


##############
# Solution 5 #
##############

def fibonacci_5(n):
    fib = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]

    for i in range(n):
        matrix_mult(res, fib)

    return res[1][1] # Fn-1 (or change the range(n-1) and use res[0][1] or res[1][0])


##############
# Solution 6 #
##############

def fibonacci_6(n):
    res = [[1, 1], [1, 0]]

    matrix_pow(res, n + 1)

    return res[1][1] # return Fn-1

def matrix_pow(mat, n):
    # divide and conquer power function
    if (n == 0) or (n == 1):
        return

    # split on 2, because matrix^k = matrix^(k/2) * matrix^(k/2)
    matrix_pow(mat, n // 2)

    matrix_mult(mat, mat)
    if n % 2 == 1:
        # multiply by the start matrix if odd power
        matrix_mult(mat, [[1, 1], [1, 0]])


##############
# Solution 7 #
##############

def fibonacci_7(n):
    fib = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2 == 1:
            matrix_mult(res, fib)

        n = n // 2
        matrix_mult(fib, fib)

    return res[1][1]


###########
# Testing #
###########

# Test 1
# Correct result => 21
print(fibonacci_1(8))
print(fibonacci_2(8))
print(fibonacci_3(8))
print(fibonacci_4(8))
print(fibonacci_5(8))
print(fibonacci_6(8))
print(fibonacci_7(8))


# Test 2
# Correct result => 10946
print(fibonacci_1(21))
print(fibonacci_2(21))
print(fibonacci_3(21))
print(fibonacci_4(21))
print(fibonacci_5(21))
print(fibonacci_6(21))
print(fibonacci_7(21))
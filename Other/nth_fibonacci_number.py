'''
Find Nth Fibonacci Number

The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
Given a number n, print n-th Fibonacci Number.

Input: 8
Output: 34

=========================================
Many solutions for this problem exist, I'll show 7 different solutions,
starting from the worst, O(2^N) time complexity, and finishg with the best, O(LogN) time complexity.

The simplest recursive solution. Direct recursive implementation of this
mathematical recurrence relation T(N) = T(N-1) + T(N-2).
Everyone knows this, this is the introductory lesson in recursion.
    Time Complexity:    O(2^N)  , actually ~1.6^N, the golden ratio number
    Space Complexity:   O(N)    , because of the recursion stack

Recursion with memoization, much faster, less computations.
For many numbers the recursive function is called more than once (in total ~1.6^N - N times duplicate calls).
Use hashmap/dictionary to save all computed numbers as values and the positions as keys.
    Time Complexity:    O(N)
    Space Complexity:   O(N)

Dynamic programming. Implementation of T(N) = T(N-1) + T(N-2) using a loop and dp table/array.
    Time Complexity:    O(N)
    Space Complexity:   O(N)

Space optimized dynamic programming. You can easily notice that you don't need the whole array,
you need only the last 2 values T(N-1) and T(N-2), and after you compute T(N) you won't need T(N-2) anymore, etc.
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Using power of the matrix [[1, 1], [1, 0]]. The 3 next solutions are based on this logic.
Explanation:
start matrix:   | 1  1 |
                | 1  0 |

result matrix:  | Fn+1  Fn   |
                | Fn    Fn-1 |

result * start =    | Fn+1 * 1 + Fn * 1    Fn+1 * 1 + Fn * 0 |
                    | Fn * 1 + Fn-1 * 1    Fn * 1 + Fn-1 * 0 |

               =    | Fn+1 + Fn    Fn+1 |
                    | Fn + Fn-1    Fn   |

               =    | Fn+2    Fn+1 |
                    | Fn+1    Fn   |
According to this, when you're multiplying with this matrix you're getting the next fibonacci number.
    Time Complexity:    O(N)
    Space Complexity:   O(1)

Time optimized matrix power. Using a recursive divide and conquer approach.
From the basic math we know that A^K * A^K = A^2K, the same rule we can use in matrix multiplication.
    Time Complexity:    O(LogN)
    Space Complexity:   O(LogN)     , because of the recursion stack

Time and space optimized matrix multiplication.
Using a loop (without a recursion) compute the power of N of the matrix.
    Time Complexity:    O(LogN)
    Space Complexity:   O(1)

Using the golden ratio (Binet's formula) = (1+sqrt(5))/2 ~ 1.6183...
More info about this solution: https://demonstrations.wolfram.com/GeneralizedFibonacciSequenceAndTheGoldenRatio/
    Time Complexity:    O(1)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def nth_fibonacci_1(n):
    if n == 0 or n == 1:
        return n

    return nth_fibonacci_1(n - 1) + nth_fibonacci_1(n - 2)


##############
# Solution 2 #
##############

# all found fibonacci numbers and positions
fib = {0: 0, 1: 1}

def nth_fibonacci_2(n):
    # check if the value is already found
    if n in fib:
        return fib[n]

    # save the fibonacci value for N position
    fib[n] = nth_fibonacci_2(n - 1) + nth_fibonacci_2(n - 2)

    return fib[n]


##############
# Solution 3 #
##############

def nth_fibonacci_3(n):
    dp = [0] * max(2, n+1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


##############
# Solution 4 #
##############

def nth_fibonacci_4(n):
    dp0, dp1 = 0, 1

    for i in range(n):
        dp0, dp1 = dp1, dp0 + dp1 # "Pythonic way"
        # or dp1 += dp0; dp0 = dp1 - dp0; in other languages

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
    a[0] is the first row of a, which contains a[0][0], a[0][1]
    Python "unrolls" a00, a01 = a[0], which effectively makes it:
    a00 = a[0][0] and a01 = a[0][1]
    '''
    a00, a01 = a[0]
    a10, a11 = a[1]
    b00, b01 = b[0]
    b10, b11 = b[1]
    a[0][0] = a00 * b00 + a01 * b10
    a[0][1] = a00 * b01 + a01 * b11
    a[1][0] = a10 * b00 + a11 * b10
    a[1][1] = a10 * b01 + a11 * b11


##############
# Solution 5 #
##############

def nth_fibonacci_5(n):
    fib = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]

    for i in range(n):
        matrix_mult(res, fib)

    return res[1][1] # Fn-1 (or change the range(n-1) and use Fn => res[0][1] or res[1][0])


##############
# Solution 6 #
##############

def nth_fibonacci_6(n):
    res = [[1, 1], [1, 0]]

    matrix_pow(res, n + 1)

    return res[1][1]

def matrix_pow(mat, n):
    if n == 0 or n == 1:
        return

    # first compute the power of n/2
    matrix_pow(mat, n // 2)

    # after that you can compute power of n, mat^(n/2) * mat^(n/2) = mat^n
    matrix_mult(mat, mat)

    if n % 2 == 1:
        # multiply by the start matrix if odd power
        matrix_mult(mat, [[1, 1], [1, 0]])


##############
# Solution 7 #
##############

def nth_fibonacci_7(n):
    fib = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]

    while n > 0:
        if n % 2 == 1:
            matrix_mult(res, fib)

        n = n // 2
        matrix_mult(fib, fib)

    return res[1][1]


##############
# Solution 8 #
##############

import math

def nth_fibonacci_8(n):
    golden_ratio = (1 + math.sqrt(5)) / 2
    return int((1 + math.pow(golden_ratio, n)) / math.sqrt(5))
    # without math module, using ** operator
    # golden_ratio = (1 + 5 ** 0.5) / 2
    # return int((1 + golden_ratio ** n) / (5 ** 0.5))


###########
# Testing #
###########

# Test 1
# Correct result => 21
n = 8
print(nth_fibonacci_1(n))
print(nth_fibonacci_2(n))
print(nth_fibonacci_3(n))
print(nth_fibonacci_4(n))
print(nth_fibonacci_5(n))
print(nth_fibonacci_6(n))
print(nth_fibonacci_7(n))
print(nth_fibonacci_8(n))

# Test 2
# Correct result => 10946
n = 21
print(nth_fibonacci_1(n))
print(nth_fibonacci_2(n))
print(nth_fibonacci_3(n))
print(nth_fibonacci_4(n))
print(nth_fibonacci_5(n))
print(nth_fibonacci_6(n))
print(nth_fibonacci_7(n))
print(nth_fibonacci_8(n))
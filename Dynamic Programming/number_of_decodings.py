'''
Number of Decodings

Given the mapping a=1, b=2, ... , z=26, and an encoded message, count the number of ways it can be decoded.
For example, the message "111" would give 3, since it could be decoded as "aaa", "ka" and "ak".
All of the messages are decodable!

=========================================
The easiest solution is Brute-Force (building a tree and making all combinations),
and in the worst case there will be Fibbionaci(N) combinations, so the worst Time Complexity will be O(Fib(N))

Dynamic programming solution. Similar to number_of_smses.py.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def num_decodings(code):
    n = len(code)
    dp = [0 for i in range(n)]

    if n == 0:
        return 0
    dp[0] = 1
    if n == 1:
        return dp[0]
    dp[1] = (code[1] != '0') + is_valid(code[0:2])

    for i in range(2, n):
        if code[i] != '0':
            # looking for how many combinations are there till now if this is a single digit
            dp[i] += dp[i-1]
        if is_valid(code[i-1 : i+1]):
            # looking for how many combinations are there till now if this is a number of 2 digits
            dp[i] += dp[i-2]

    return dp[n-1]

def is_valid(code):
    k = int(code)
    return (k < 27) and (k > 9)


###########
# Testing #
###########

# Test 1
# Correct result => 5
print(num_decodings('12151'))

# Test 2
# Correct result => 5
print(num_decodings('1111'))

# Test 3
# Correct result => 3
print(num_decodings('111'))

# Test 4
# Correct result => 1
print(num_decodings('1010'))

# Test 5
# Correct result => 4
print(num_decodings('2626'))

# Test 6
# Correct result => 1
print(num_decodings('1'))

# Test 7
# Correct result => 2
print(num_decodings('11'))

# Test 8
# Correct result => 3
print(num_decodings('111'))

# Test 9
# Correct result => 5
print(num_decodings('1111'))

# Test 10
# Correct result => 8
print(num_decodings('11111'))

# Test 11
# Correct result => 13
print(num_decodings('111111'))

# Test 12
# Correct result => 21
print(num_decodings('1111111'))

# Test 13
# Correct result => 34
print(num_decodings('11111111'))
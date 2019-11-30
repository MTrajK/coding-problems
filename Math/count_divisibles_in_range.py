'''
Count Divisibles in Range

Let us take a breather and tackle a problem so simple that its solution needs only a couple of
conditions, but not even any loops, let alone anything even more fancy. The difficulty is coming up
with the conditions that cover all possible cases of this problem exactly right, including all of the
potentially tricksy edge and corner cases, and not be off-by-one. Given three integers start, end
and n so that start <= end, count and return how many integers between start and end,
inclusive, are divisible by n.

Input: 7, 28, 4
Output: 6

=========================================
Find the close divisible to start (the smallest divisible in the range), calculate the difference between
that number and the end of the range, and in the end divide the difference by N.
    Time Complexity:    O(1)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def count_divisibles_in_range(start, end, n):
    # find the next start number divisable by n
    start += (n - (start % n)) % n

    if start > end:
        # in this case there are no numbers divisable by n
        return 0

    return 1 + ((end - start) // n)


###########
# Testing #
###########

# Test 1
# Correct result => 6
print(count_divisibles_in_range(7, 28, 4))

# Test 2
# Correct result => 9
print(count_divisibles_in_range(-77, 19, 10))

# Test 3
# Correct result => 0
print(count_divisibles_in_range(-19, -13, 10))

# Test 4
# Correct result => 199999999999
print(count_divisibles_in_range(1, 10**12 - 1, 5))

# Test 5
# Correct result => 200000000000
print(count_divisibles_in_range(0, 10**12 - 1, 5))

# Test 6
# Correct result => 200000000001
print(count_divisibles_in_range(0, 10**12, 5))
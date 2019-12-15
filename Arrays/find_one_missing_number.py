'''
Find the missing number in a sequence

Find the only missing integer in a sequence,
all numbers are integers and they're smaller or equal to N+1 (N is length of the array).

Input: [2, 1, 4]
Output: 3

=========================================
Searching for 1 unknown, math problem.
Use the sum formula for the first N numbers to compute the whole sum of the sequence.
After that sum all elements from the array, and when you subtract those 2 numbers, you'll get the missing number.
Sum formula = N*(N+1)/2
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''

############
# Solution #
############

def missing_number(nums):
    s = sum(nums)
    n = len(nums) + 1
    # sum formula (sum of the first n numbers) = (N*(N+1))/2
    return n * (n + 1) // 2 - s


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(missing_number([2, 3, 1]))

# Test 2
# Correct result => 3
print(missing_number([2, 1, 4]))
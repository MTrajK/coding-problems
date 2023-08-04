'''
Reverse Array in groups

Given an Array of size N. Modify the array in-place by reversing every sub-array of size K.

Note : If at any instance, there are no more subarrays of size greater than or equal to K, 
        then reverse the last subarray (irrespective of its size).
        You shouldn't return any array, modify the given array in-place.

Input: [1, 2, 3, 4, 5]
Output: [3, 2, 1, 5, 4]
Output explanation: 1, 2, 3 => 3, 2, 1; 4, 5 => 5, 4

=========================================
Find the start and end of each sublist and reverse it in-place.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def reverse_array_in_groups(arr, k):
    # Initialize a variable to keep track of sub arrays of length k
    i = 0
    n = len(arr)
    while i<n:
        # The sub-array can be of length k or less so the right index in chosen accordingly
        left = i
        right = min(i+k-1, n-1)
        while left < right:
            # After finding the required indices we reverse the array by swapping two elements at a time
            arr[left], arr[right] = arr[right], arr[left]
            # Increasing the left index and decreasing the right index.
            left += 1
            right -= 1
        # After succesfully reversing one sub-array move to next by increasing i by a value of k.
        i += k
    return arr


###########
# Testing #
###########

# Test 1
# Correct result => [3, 2, 1, 5, 4]
print(reverse_array_in_groups([1, 2, 3, 4, 5], 3))

# Test 2
# Correct result => [2, 3, 4, 5, 1]
print(reverse_array_in_groups([5, 4, 3, 2, 1], 4))

# Test 3
# Correct result => [10, 7, 5, 7, 2, 4, 3, 1, 8]
print(reverse_array_in_groups([5, 7, 10, 4, 2, 7, 8, 1, 3], 3))

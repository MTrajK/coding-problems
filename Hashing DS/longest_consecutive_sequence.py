'''
Longest Consecutive Sequence (Largest Range)

Short explanation: Given an unsorted array of integers, find first and last element
of the longest consecutive elements sequence.

Long explanation: Write a function that takes in an array of integers and returns an array of
length 2 representing the largest range of numbers contained in that array.
The first number in the output array should be the first number in the range while the second number
should be the last number in the range. A range of numbers is defined as a set of numbers
that come right after each other in the set of real integers.
For instance, the output array [2, 6] represents the range {2, 3, 4, 5, 6}, which is a range of length 5.
Note that numbers do not need to be ordered or adjacent in the array in order to form a range.

Input: [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
Output: [0, 7]

=========================================
The simplest solution is to sort the array, that's O(N LogN) time complexity.

But this solution is faster, it uses a dictionary (HashMap).
For each number tries to find the smaller and the bigger consequence numbers, and marks them as visited.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def largest_range(array):
    visited = {}
    for el in array:
        visited[el] = False

    max_range = [array[0], array[0]]
    for el in array:
        if visited[el]:
            # this element is visited in another range, no need from searching again for this range
            continue

        visited[el] = True

        # go left
        left_border = el - 1
        while left_border in visited:
            visited[left_border] = True
            left_border -= 1
        # update the left_border because that number doesn't exist
        left_border += 1

        # go right
        right_border = el + 1
        while right_border in visited:
            visited[right_border] = True
            right_border += 1
        # update the right_border because that number doesn't exist
        right_border -= 1

        if (max_range[1] - max_range[0]) < (right_border - left_border):
            max_range = [left_border, right_border]

    return max_range


###########
# TESTING #
###########

# Test 1
# Correct result => [-1, 19]
print(largest_range([0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14]))

# Test 2
# Correct result => [-7, 7]
print(largest_range([0, -5, 9, 19, -1, 18, 17, 2, -4, -3, 10, 3, 12, 5, 16, 4, 11, 7, -6, -7, 6, 15, 12, 12, 2, 1, 6, 13, 14, -2]))

# Test 3
# Correct result => [-8, 19]
print(largest_range([-7, -7, -7, -7, 8, -8, 0, 9, 19, -1, -3, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, -6, 8, 7, 6, 15, 12, 12, -5, 2, 1, 6, 13, 14, -4, -2]))
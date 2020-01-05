'''
Reverse array

Reverse an array, in constant space and linear time complexity.

Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

=========================================
Reverse the whole array by swapping pair letters in-place (first with last, second with second from the end, etc).
Exist 2 more "Pythonic" ways of reversing arrays/strings (but not in-place, they're creating a new list):
- reversed_arr = reversed(arr)
- reversed_arr = arr[::-1]
But I wanted to show how to implement a reverse algorithm step by step so someone will know how to implement it in other languages.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def reverse_arr(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # reverse the array from the start index to the end index by
        # swaping each element with the pair from the other part of the array
        swap(arr, start, end)
        start += 1
        end -= 1

    return arr

def swap(arr, i, j):
    # swapping two elements from a same array
    arr[i], arr[j] = arr[j], arr[i]
    '''same as
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    '''


###########
# Testing #
###########

# Test 1
# Correct result => [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(reverse_arr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Test 2
# Correct result => [5, 4, 3, 2, 1]
print(reverse_arr([1, 2, 3, 4, 5]))
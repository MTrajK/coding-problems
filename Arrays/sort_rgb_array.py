'''
Sort RGB Array

Given an array of strictly the characters 'R', 'G', and 'B', segregate
the values of the array so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the array.
Do this in linear time and in-place.

Input: ['G', 'B', 'R', 'R', 'B', 'R', 'G']
Output: ['R', 'R', 'R', 'G', 'G', 'B', 'B']

=========================================
Play with pointers/indices and swap elements. (only one iteration)
Save the last R, G and B indices, when adding some color, move the rest indices by 1.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
Count R, G, B and populate the array after that. (2 iterations)
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def sort_rgb_array(arr):
    n = len(arr)

    # indexes/pointers of the last element of each color
    r, g, b = 0, 0, 0

    for i in range(n):
        # swap the element and move the pointer
        if arr[i] == 'R':
            swap(arr, i, r)
            r += 1

        # move pointer
        if r > g:
            g = r

        # swap the element and move the pointer
        if arr[i] == 'G':
            swap(arr, i, g)
            g += 1

        # move pointer
        if g > b:
            b = g

        # swap the element and move the pointer
        if arr[i] == 'B':
            swap(arr, i, b)
            b += 1

    return arr

def swap(arr, i, j):
    # swaps two elements in an array
    arr[i], arr[j] = arr[j], arr[i]


##############
# Solution 2 #
##############

def sort_rgb_array_2(arr):
    rgb = {
        'R': 0,
        'G': 0,
        'B': 0
    }

    # count colors
    for c in arr:
        rgb[c] += 1

    # adjust the intervals
    rgb['G'] += rgb['R']
    rgb['B'] += rgb['G']

    # assign colors
    for i in range(len(arr)):
        if i < rgb['R']:
            arr[i] = 'R'
        elif i < rgb['G']:
            arr[i] = 'G'
        else:
            arr[i] = 'B'

    return arr


###########
# Testing #
###########

# Test 1
# Correct result => ['R', 'R', 'R', 'G', 'G', 'B', 'B']
print(sort_rgb_array(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(sort_rgb_array_2(['G', 'B', 'R', 'R', 'B', 'R', 'G']))

# Test 2
# Correct result => ['R', 'R', 'G', 'G', 'B', 'B', 'B']
print(sort_rgb_array(['B', 'B', 'B', 'G', 'G', 'R', 'R']))
print(sort_rgb_array_2(['B', 'B', 'B', 'G', 'G', 'R', 'R']))
'''
Find the element before which all the elements are smaller than it, and after which all are greater

Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.

Input: [5, 1, 4, 3, 6, 8, 10, 7, 9]
Output: 6

=========================================
Traverse the array starting and check if the current element is smaller than the wanted one. If it's smaller then reset the result.
In meantime keep track of the maximum value till the current position. This maximum value will be used for finding a new "middle" element.
If the maximum value
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def find_element_smaller_left_bigger_right(arr):
    n = len(arr)
    curr_max = arr[0]
    result = -1

    for i in range(1, n):
        curr_el = arr[i]

        if result == -1 and curr_el >= curr_max and i != n - 1:
            result = curr_el
        elif curr_el < result:
            result = -1

        if curr_el > curr_max:
            curr_max = curr_el

    return result

###########
# Testing #
###########

# Test 1
# Correct result => 6
print(find_element_smaller_left_bigger_right([5, 1, 4, 3, 6, 8, 10, 7, 9]))

# Test 2
# Correct result => -1
print(find_element_smaller_left_bigger_right([5, 1, 4, 4]))

# Test 3
# Correct result => 7
print(find_element_smaller_left_bigger_right([5, 1, 4, 6, 4, 7, 14, 8, 19]))

# Test 4
# Correct result => 5
print(find_element_smaller_left_bigger_right([4, 2, 5, 7]))

# Test 5
# Correct result => -1
print(find_element_smaller_left_bigger_right([11, 9, 12]))

# Test 6
# Correct result => 234
print(find_element_smaller_left_bigger_right([177, 234, 236, 276, 519, 606, 697, 842, 911, 965, 1086, 1135, 1197, 1273, 1392, 1395, 1531, 1542, 1571, 1682, 2007, 2177, 2382, 2410, 2432, 2447, 2598, 2646, 2672, 2826, 2890, 2899, 2916, 2955, 3278, 3380, 3623, 3647, 3690, 4186, 4300, 4395, 4468, 4609, 4679, 4712, 4725, 4790, 4851, 4912, 4933, 4942, 5156, 5186, 5188, 5244, 5346, 5538, 5583, 5742, 5805, 5830, 6010, 6140, 6173, 6357, 6412, 6414, 6468, 6582, 6765, 7056, 7061, 7089, 7250, 7275, 7378, 7381, 7396, 7410, 7419, 7511, 7625, 7639, 7655, 7776, 7793, 8089, 8245, 8622, 8758, 8807, 8969, 9022, 9149, 9150, 9240, 9273, 9573, 9938]))

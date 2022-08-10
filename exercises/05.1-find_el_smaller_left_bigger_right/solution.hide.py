############
# Solution #
############

import math

def find_element_smaller_left_bigger_right(arr):
    n = len(arr)
    left_maxs = [-math.inf]
    right_min = math.inf

    # find all mins from the front
    for i in range(n - 1):
        left_maxs.append(max(left_maxs[-1], arr[i]))

    for i in range(n - 1, -1, -1):
        # check if all left are smaller
        # and all right are bigger
        if (left_maxs[i] < arr[i]) and (right_min > arr[i]):
            return i

        # don't need a separate for loop for this as mins
        right_min = min(right_min, arr[i])

    return -1


print(find_element_smaller_left_bigger_right([5, 1, 4, 3, 6, 8, 10, 7, 9]))

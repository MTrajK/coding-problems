'''
Trapped Water

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

Input: [2, 1, 2]
Output: 1
Output explanation: We can hold 1 unit of water in the middle.

Input: [3, 0, 1, 3, 0, 5]
Output: 8
Output explanation: We can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

=========================================
The goal is to find the max wall and make 2 iterations starting from front and from back looking for the next bigger wall.
First search for the max wall from front, after that correct the left water starting from the back side
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def trapped_water(elevation_map):
    n = len(elevation_map)
    if n == 0:
        return 0

    water = 0

    # start from front of the array
    # and look for the max wall
    max_idx = 0
    max_height = elevation_map[0]

    for i in range(1, n):
        if elevation_map[i] >= max_height:
            max_idx = i # save the highest wall index for later
            max_height = elevation_map[i]

        water += max_height - elevation_map[i]

    # after that start from back and go reverse to the max wall idx
    # and correct the result (pour the extra water if there is smaller wall on the right side)
    back_max_height = elevation_map[-1]

    for i in range(n - 1, max_idx, -1):
        if elevation_map[i] > back_max_height:
            back_max_height = elevation_map[i]

        water -= max_height - back_max_height

    return water


###########
# Testing #
###########

# Test 1
# Correct result => 1
print(trapped_water([2, 1, 2]))

# Test 2
# Correct result => 8
print(trapped_water([3, 0, 1, 3, 0, 5]))

# Test 3
# Correct result => 6
print(trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
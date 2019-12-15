'''
Permutations

Given a collection of distinct integers, return all possible permutations.

Input: [1,2,3]
Output: 
        [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]

=========================================
A classical recursive algorithm for  permutations.
    Time Complexity:    O(N!)
    Space Complexity:   O(N!)
'''


############
# Solution #
############

def permutations(nums):
    result = []
    if len(nums) == 0:
        return result

    permute(result, set(nums), [])

    return result

def permute(result, nums, permutation):
    if len(nums) == 0:
        result.append([num for num in permutation])
    else:
        for num in list(nums): # create a new object with the same values because nums will be changed later
            nums.remove(num)
            permutation.append(num)

            permute(result, nums, permutation)

            # reset the structures
            del permutation[-1]
            nums.add(num)


###########
# Testing #
###########

# Test 1
# Correct result => [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(permutations([1, 2, 3]))
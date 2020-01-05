'''
Min Swaps

You have a list of numbers and you want to sort the list.
The only operation you have is a swap of any two arbitrary numbers.
Find the minimum number of swaps you need to do in order to make the list sorted (ascending order).
- The array will contain N elements
- Each element will be between 1 and N inclusive
- All the numbers will be different

Input: [4, 1, 3, 2]
Output: 2
Output explanation: swap(4, 1) = [1, 4, 3, 2], swap(4, 2) = [1, 2, 3, 4]

=========================================
According to the description, all elements will have their position in the array,
for example, K should be located at K-1 in the array.
Itterate the array and check if each position has the right element,
if not, put that element in the right position and check again.
    Time Complexity:    O(N)    , the solution looks like O(N^2) but that's not possible, at most O(2*N) operations can be done
    Space Complexity:   O(1)
'''


############
# Solution #
############

def min_swaps(a):
    n = len(a)
    swaps = 0

    for i in range(n):
        # swap the elements till the right element isn't found
        while a[i] - 1 != i:
            swap = a[i] - 1
            # swap the elements
            a[swap], a[i] = a[i], a[swap]

            swaps += 1

    return swaps


###########
# Testing #
###########

# Test 1
# Correct result => 2
print(min_swaps([4, 1, 3, 2]))

# Test 2
# Correct result => 3
print(min_swaps([4, 1, 2, 3]))
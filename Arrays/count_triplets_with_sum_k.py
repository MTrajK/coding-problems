'''
Count Triplets with Sum K

Given an array (sorted in ascending order) and a value, count how many triplets
exist in array whose sum is equal to the given value.

Input: [1, 2, 3, 4, 5], 9
Output: 2
Output explanation: (1, 3, 5) and (2, 3, 4)

=========================================
Fix the first element (i), move the second element (j) and search into the hashset.
(similar approach to find_pairs_with_sum_k.py)
    Time Complexity:    O(N^2)
    Space Complexity:   O(N)
Fix the first element (i), and play with 2 pointers from the left (i+1) and right (n-1) side.
If the current sum is smaller than K then increase the left pointer, otherwise decrease the right pointer.
* This solution works only for elements in sorted ascending order. If the elements aren't sorted, first sort
them and after that use this algorithm, the time complexity will be same O(NLogN + N^2) = O(N^2).
    Time Complexity:    O(N^2)
    Space Complexity:   O(1)
'''


##############
# Solution 1 #
##############

def count_triplets_1(arr, k):
    count = 0
    n = len(arr)

    for i in range(n - 2):
        elements = set()
        curr_sum = k - arr[i]

        for j in range(i + 1, n):
            if (curr_sum - arr[j]) in elements:
                count += 1
            elements.add(arr[j])

    return count


##############
# Solution 2 #
##############

def count_triplets_2(arr, k):
    count = 0
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            if curr_sum == k:
                count += 1
                right -= 1
            elif curr_sum < k:
                left += 1
            else:
                right -= 1

    return count


###########
# Testing #
###########

# Test 1
# Correct result => 1
arr = [10, 11, 16, 18, 19]
k = 40
print(count_triplets_1(arr, k))
print(count_triplets_2(arr, k))

# Test 2
# Correct result => 2
arr = [1, 2, 3, 4, 5]
k = 9
print(count_triplets_1(arr, k))
print(count_triplets_2(arr, k))
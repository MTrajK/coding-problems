'''
Find an Element Which is Smaller or Equal to Exactly K Numbers

You have to find some number X greater than 0 where exactly K elements in that list are greater than or equal to the number X.
If there are multiple such values return the smallest possible.
If there is no such X, return (-1).

Input: [3,8,5,1,10,3,20,24], 2
Output: 11
Output explanation: Only 20 and 24 are equal or smaller from 11 (11 is the smallest solution, also 12, 13...20 are solutions).

=========================================
Sort the array and check the Kth element from the end.
    Time Complexity:    O(NLogN)
    Space Complexity:   O(1)
QuickSelect can be used (find the K+1th number + 1). https://en.wikipedia.org/wiki/Quickselect
See kth_smallest.py, very similar solution.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def get_minimum_X(arr, k):
    n = len(arr)

    if n == 0 or k > n:
        return -1

    if k == n:
        return 1

    arr.sort()

    if k == 0:
        return arr[-1] + 1

    if arr[-k] == arr[-(k + 1)]:
        return -1

    return arr[-(k + 1)] + 1


###########
# Testing #
###########

# Test 1
# Correct result => 11
print(get_minimum_X([3, 8, 5, 1, 10, 3, 20, 24], 2))

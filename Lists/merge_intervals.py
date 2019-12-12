'''
Merge Intervals

You are given an array of intervals.
Each interval is defined as: (start, end). e.g. (2, 5)
It represents all the integer numbers in the interval, including start and end. (in the example 2, 3, 4 and 5).
Given the array of intervals find the smallest set of unique intervals that contain the same integer numbers, without overlapping.


Input: [(1, 5), (2, 6)]
Output: [(1, 6)]

Input: [(2, 4), (5, 5), (6, 8)]
Output: [(2, 8)]

Input: [(1, 4), (6, 9), (8, 10)]
Output: [(1, 4), (6, 10)]

=========================================
Sort the intervals (using the start), accessing order. After that just iterate the intervals
and check if the current interval belongs to the last created interval.
    Time Complexity:    O(N LogN)
    Space Complexity:   O(N)    , for the result
'''


############
# Solution #
############

def merge_intervals(intervals):
    n = len(intervals)
    if n == 0:
        return []

    # sort the intervals
    intervals.sort(key=lambda interval: interval[0])
    mergedIntervals = []
    mergedIntervals.append(intervals[0])

    for i in range(1, n):
        # check if this interval belongs to the last created interval
        if intervals[i][0] <= mergedIntervals[-1][1] + 1:
            # only the end can be changed (just copy start it's min, because the array is sorted)
            mergedIntervals[-1] = (mergedIntervals[-1][0], max(mergedIntervals[-1][1], intervals[i][1]))
        else:
            # create a new interval
            mergedIntervals.append(intervals[i])

    return mergedIntervals


###########
# Testing #
###########

# Test 1
# Correct result => [(1, 6)]
print(merge_intervals([(1, 5), (2, 6)]))

# Test 2
# Correct result => [(2, 8)]
print(merge_intervals([(2, 4), (5, 5), (6, 8)]))

# Test 3
# Correct result => [(1, 4), (6, 10)]
print(merge_intervals([(1, 4), (6, 9), (8, 10)]))
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
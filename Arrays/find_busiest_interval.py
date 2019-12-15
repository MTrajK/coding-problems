'''
Find the Busiest Interval

Given a list of arriving time and leaving time for each celebrity.
Celebrity I, arrives at arriving[I] time and leaves at leaving[I] time.
Output is the time interval that you want to go the party when the maximum number of celebrities are still there.

Input: arriving=[30, 0, 60], leaving=[75, 50, 150]
Output: (30, 50) or (60, 75)

=========================================
Just sort the lists, don't care about pairs ordering.
And use a counter, when arriving counter++, when leaving counter--.
    Time Complexity:    O(N LogN)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def bussiest_interval(arriving, leaving):
    # sort both arrays (don't care about pairs)
    arriving.sort()
    leaving.sort()

    n = len(arriving)
    i, j = 0, 0
    start, end = 0, 0
    overlapping = 0
    max_overlapping = 0

    # both arrays have same number of elements
    # but the biggest time is from the leaving array
    # becayse of that you're sure that 'i' will reach the end before 'j'
    while i < n:
        if arriving[i] <= leaving[j]:
            overlapping += 1
            if max_overlapping <= overlapping:
                max_overlapping = overlapping
                # save the start time if max_overlapping
                start = arriving[i]
            i += 1
        else:
            if max_overlapping == overlapping:
                # save the exit time if max_overlapping
                end = leaving[j]
            overlapping -= 1
            j += 1

    # check again this to close the result interval because 'i' is completed and not 'j'
    if max_overlapping == overlapping:
        end = leaving[j]

    # return start&end or max_overlapping
    return (start, end)


###########
# Testing #
###########

# Test 1
# Correct result => (30, 50) or (60, 75)
print(bussiest_interval([30, 0, 60], [75, 50, 150]))

# Test 2
# Correct result => (5, 5)
print(bussiest_interval([1, 2, 10, 5, 5], [4, 5, 12, 9, 12]))
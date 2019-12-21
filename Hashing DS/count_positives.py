'''
Count Positives

Given several numbers, count how many different results bigger or equal than 0 can you produce by only
using addition (+) and substraction (-). All the numbers must be used.

Input: [2, 3, 1]
Output: 4
Output explanation:
        2+3+1 = 6
        2+3-1 = 4
        2-3+1 = 0
        2-3-1 = -2 (negative)
        -2+3+1 = 2
        -2+3-1 = 0 (double)
        -2-3+1 = -4 (negative)
        -2-3-1 = - 6 (negative)

=========================================
Use hashset and make all combinations.
    Time Complexity:    O(2^N)  , I'm not sure how to compute the real complexity, but it's TOO MUCH faster than 2^N
    Space Complexity:   O(2^N)
'''


############
# Solution #
############

def count_positives(numbers):
    results = set()
    results.add(0)

    # make all combinations
    for num in numbers:
        temp = set()    # use a temporary hashset for the newest results
        for res in results:
            temp.add(res + num)
            temp.add(res - num)
        results = temp  # replace the results

    # count unique positives
    count = 0
    for res in results:
        if res >= 0:
            count += 1

    return count


###########
# Testing #
###########

# Test 1
# Correct result => 4
print(count_positives([2, 3, 1]))
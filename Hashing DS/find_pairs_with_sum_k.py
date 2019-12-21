'''
Find pairs with sum K

Given an array, find all pairs which sum is equal to K.

Input: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9], 5
Output: [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]

=========================================
Save numbers as complements in a hashset and for each number search for the pair complement (K-number).
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def find_pairs(arr, K):
    # set to save all complements
    complements = set()
    # set to save all unique complements that form a pair
    pair_complements = set()

    for el in arr:
        c = K - el

        # if complement exists, then a pair is found
        if c in complements:
            pair_complements.add(c)

        # save this number as complement
        complements.add(el)

    # find all unique pairs
    pairs = []
    for c in pair_complements:
        pairs.append((c, K - c))

    return pairs


###########
# Testing #
###########

# Test 1
# Correct result => [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
print(find_pairs([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9], 10))
'''
Reverse string

Reverse string, in linear time complexity.

Input: 'i like this program very much'
Output: 'hcum yrev margorp siht ekil i'

Input: 'how are you'
Output: 'uoy era woh'

=========================================
Reverse the whole sentence by swapping pair letters in-place (first with last, second with second from the end, etc).
In Python, the string manipulation operations are too slow (string is immutable), because of that we need to convert the string into array.
In C/C++, the Space complexity will be O(1) (because the strings are just arrays with chars).
Exist 2 more "Pythonic" ways of reversing strings/arrays:
- reversed_str = reversed(str)
- reversed_str = str[::-1]
But I wanted to show how to implement a reverse algorithm step by step so someone will know how to implement it in other languages.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def reverse_sentence(sentence):
    arr = [c for c in sentence] # or just arr = list(sentence)
    start = 0
    end = len(arr) - 1

    while start < end:
        # reverse the array from the start index to the end index by
        # swaping each char with the pair from the other part of the array
        swap(arr, start, end)
        start += 1
        end -= 1

    return ''.join(arr)

def swap(arr, i, j):
    # swapping two elements from a same array
    arr[i], arr[j] = arr[j], arr[i]
    '''same as
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    '''


###########
# Testing #
###########

# Test 1
# Correct result => 'hcum yrev margorp siht ekil i'
print(reverse_sentence('i like this program very much'))

# Test 2
# Correct result => 'uoy era woh'
print(reverse_sentence('how are you'))
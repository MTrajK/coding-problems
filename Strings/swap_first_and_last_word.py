'''
Swap the frst and the last word

Given an string, you need to swap the first and last word in linear time.
Everything between should stay in same order.

Sample input: 'i like this program very much'
Sample output: 'much like this program very i'

=========================================
Reverse the whole string, after that reverse only first and only last word,
in the end reverse everything between first and last word. (using IN-PLACE reversing)
In Python, the string manipulation operations are too slow (string is immutable), because of that we need to convert the string into array.
In C/C++, the Space complexity will be O(1) (because the strings are just arrays with chars).
    Time complexity:    O(N)    , O(N + N) = O(2 * N) = O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def swap_first_and_last_word(sentence):
    arr = [c for c in sentence] # or just arr = list(sentence)
    first_idx = 0
    last_idx = len(arr) - 1

    # reverse the whole array, in this way I'll change the first and the last word
    reverse_array(arr, first_idx, last_idx)

    # find positions of the first and the last space char
    first_space = first_idx
    while arr[first_space] != ' ':
        first_space += 1

    last_space = last_idx
    while arr[last_space] != ' ':
        last_space -= 1

    # reverse only the first word
    reverse_array(arr, first_idx, first_space - 1)
    # reverse only the last word
    reverse_array(arr, last_space + 1, last_idx)
    # reverse everything between (with this reversing, all words between will have the same order as the starting one)
    reverse_array(arr, first_space + 1, last_space - 1)

    return ''.join(arr)

def reverse_array(arr, start, end):
    # reverse the array from the start index to the end index
    while start < end:
        arr[start], arr[end] = arr[end], arr[start] # swap
        start += 1
        end -= 1


###########
# Testing #
###########

# Test 1
# Correct result => 'practice makes perfect
print(swap_first_and_last_word('perfect makes practice'))

# Test 2
# Correct result => 'much like this program very i'
print(swap_first_and_last_word('i like this program very much'))
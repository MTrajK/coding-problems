'''
swap the frst and the last word

Given an array with chars (or string/not immutable), 
you need to swap the words INPLACE (this means, that you cannot use additional array) in linear time. 
Everything between should stay in same order.

Sample input: 'perfect makes practice'
Sample output: 'practice makes perfect'

=========================================
Reverse the whole string, after that reverse only first and only last word, 
in the end reverse everything between first and last word. (using INPLACE reversing)
* Used array with chars instead string, because string in Python is immutable and everytime 
you change something inside, a new string is created.
	Time complexity:	O(N)	, O(N + N) = O(2 * N) = O(N)
	Space complexity:	O(1)
'''


############
# Solution #
############

def swap_first_and_last_word(arr):
    first_idx = 0
    last_idx = len(arr) - 1
    
    # Reverse the whole array, in this way I'll change the first and the last word
    reverse_array(arr, first_idx, last_idx)

    # Find positions of the first and the last space char
    first_space = first_idx
    while arr[first_space] != ' ':
        first_space += 1
        
    last_space = last_idx
    while arr[last_space] != ' ':
        last_space -= 1
    
    # Reverse only the first word
    reverse_array(arr, first_idx, first_space - 1)
    # Reverse only the last word
    reverse_array(arr, last_space + 1, last_idx)
    # Reverse everything between (with this reversing, all words between will have the same order as the starting one)
    reverse_array(arr, first_space + 1, last_space - 1)
    
    return arr

# Reverse the array from the start index to the end index
def reverse_array(arr, start, end):
    while start < end:
        swap(arr, start, end)
        start += 1
        end -= 1

# swapping two element from the same array
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


###########
# Testing #
###########

# Test 1
# Correct result => 'result'
array = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
print(swap_first_and_last_word(array))
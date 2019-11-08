'''
Reverse string

Reverse string, in constant space and linear time complexity.

Input: 'i like this program very much' - In Python this should be a list (the string operations are slow/linear time)
Output: 'hcum yrev margorp siht ekil i'

Input: 'how are you'
Output: 'uoy era woh'

=========================================
Reverse the whole sentence by swapping pair letters in place (first with last, second with second from the end, etc).
	Time Complexity: 	O(N)
	Space Complexity: 	O(1)
'''


############
# Solution #
############

def reverse_sentence(sentence):
    start = 0
    end = len(sentence)
    
    for i in range((end - start) // 2):
        local_start = start + i
        local_end = end - i - 1
        # swap each char with the pair from the other part of the string
        temp = sentence[local_start]
        sentence[local_start] = sentence[local_end]
        sentence[local_end] = temp


###########
# Testing #
###########

# Test 1
s = ['i', ' ', 'l', 'i', 'k', 'e', ' ', 't', 'h', 'i', 's', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 'v', 'e', 'r', 'y', ' ', 'm', 'u', 'c', 'h']
reverse_sentence(s)
# correct result => ['h', 'c', 'u', 'm', ' ', 'y', 'r', 'e', 'v', ' ', 'm', 'a', 'r', 'g', 'o', 'r', 'p', ' ', 's', 'i', 'h', 't', ' ', 'e', 'k', 'i', 'l', ' ', 'i']
print(s)

# Test 2
s = ['h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u']
reverse_sentence(s)
# correct result => ['u', 'o', 'y', ' ', 'e', 'r', 'a', ' ', 'w', 'o', 'h']
print(s)
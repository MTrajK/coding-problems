'''
Reverse words in sentence

Reverse words in a given string, in constant space and linear time complexity.

Input: 'i like this program very much' - In Python this should be a list (the string operations are slow/linear time)
Output: 'much very program this like i'

Input: 'how are you'
Output: 'you are how'

=========================================
First, find each word and reverse it (in place, by swapping the letters), 
after all words are reversed reverse the whole sentence (in place, by swapping the letters) 
and the first word will be last and in the original form.
In total, there will be only 2 iterations through the whole string.
	Time Complexity: 	O(N)
	Space Complexity: 	O(1)
'''


############
# Solution #
############

def reverse_words_in_sentence(sentence):
    n = len(sentence)
    start = 0

    # reverse all words
    for i in range(n):
        if sentence[i] == ' ':
            # in this moment you're sure that the word is complete
            reverse_word(sentence, start, i)
            start = i + 1
    # reverse the last word
    reverse_word(sentence, start, n)

    # reverse the whole sentence
    reverse_sentence(sentence)

def reverse_sentence(sentence):
    reverse_word(sentence, 0, len(sentence))

def reverse_word(sentence, start, end):
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
reverse_words_in_sentence(s)
# Correct result => ['m', 'u', 'c', 'h', ' ', 'v', 'e', 'r', 'y', ' ', 'p', 'r', 'o', 'g', 'r', 'a', 'm', ' ', 't', 'h', 'i', 's', ' ', 'l', 'i', 'k', 'e', ' ', 'i']
print(s)

# Test 2
s = ['h', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u']
reverse_words_in_sentence(s)
# Correct result => ['y', 'o', 'u', ' ', 'a', 'r', 'e', ' ', 'h', 'o', 'w']
print(s)
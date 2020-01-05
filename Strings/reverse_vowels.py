'''
Reverse Vowels

Given a text string, create and return a new string constructed by finding all its vowels (for
simplicity, in this problem vowels are the letters in the string 'aeiouAEIOU') and reversing their
order, while keeping all non-vowel characters exactly as they were in their original positions.

Input: 'Hello world'
Output: 'Hollo werld'

=========================================
Simple solution, find a vowel from left and swap it with a vowel from right.
In Python, the string manipulation operations are too slow (string is immutable), because of that we need to convert the string into array.
In C/C++, the Space complexity will be O(1) (because the strings are just arrays with chars).
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def reverse_vowels(sentence):
    arr = [c for c in sentence] # or just arr = list(sentence)

    vowels = {
        'a': True, 'A': True,
        'e': True, 'E': True,
        'i': True, 'I': True,
        'o': True, 'O': True,
        'u': True, 'U': True
    }

    left = 0
    right = len(arr) - 1

    while True:
        # find a vowel from left
        while left < right:
            if arr[left] in vowels:
                break
            left += 1

        # find a vowel from right
        while left < right:
            if arr[right] in vowels:
                break
            right -= 1

        if left >= right:
            # in this case, there are only 1 or 0 vowels
            # so this is the end of the algorithm, no need from more reversing
            break

        # swap the vowels
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return ''.join(arr)


###########
# Testing #
###########

# Test 1
# Correct result => 'ubcdofghijklmnepqrstavwxyz'
print(reverse_vowels('abcdefghijklmnopqrstuvwxyz'))

# Test 2
# Correct result => 'Hollo werld'
print(reverse_vowels('Hello world'))
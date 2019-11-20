'''
Encoding string

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.

Input: 'AAAABBBCCDAA'
Output: '4A3B2C1D2A'

=========================================
Simple solution, just iterate the string and count.
    Time Complexity:    O(N)
    Space Complexity:   O(1)
'''


############
# Solution #
############

def encoding(word):
    n = len(word)
    if n == 0:
        return ''

    letter = word[0]
    length = 1
    res = ''

    for i in range(1, n):
        if word[i] == letter:
            length += 1
        else:
            res += str(length) + letter
            letter = word[i]
            length = 1

    res += str(length) + letter

    return res


###########
# Testing #
###########

# Correct result => '4A3B2C1D2A'
print(encoding('AAAABBBCCDAA'))
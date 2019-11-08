'''
Anagram indicies

Given a word and a string S, find all starting indices in S which are anagrams of word.
(An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once)

Input: s='abxaba' word='ab'
Output: [0, 3, 4]
Output explanation: For example, given that word is 'ab', and S is 'abxaba', return 0 'ab', 3 'ab', and 4'ba'.

=========================================
Create a structure for counting the ferquency of letters (the structure is a simple dictionary).
Similar to sliding window solution, add letters into the structure from the front of sliding window
and remove from the back of sliding window.
	Time Complexity: 	O(N)
	Space Complexity: 	O(W)    , W = length of Word

Solution 2: this can be solved using Rabin–Karp algorithm (small modification of this algorithm).
But both solutions have same time & space complexity.
'''


############
# Solution #
############

class LettersCounter:
    def __init__(self):
        self.__letters = {}
    
    def __create_if_not_exist(self, letter):
        ''' helper method for creating a new field for the letter '''
        if letter not in self.__letters:
            self.__letters[letter] = 0
    
    def __delete_if_zero_letters(self, letter):
        ''' helper deleting a letter from dictionary '''
        if self.__letters[letter] == 0:
            del self.__letters[letter]
    
    def add_letter(self, letter):
        ''' increment the number of letters '''
        self.__create_if_not_exist(letter)
        self.__letters[letter] += 1
        self.__delete_if_zero_letters(letter)

    def remove_letter(self, letter):
        ''' decrement the number of letters '''
        self.__create_if_not_exist(letter)
        self.__letters[letter] -= 1
        self.__delete_if_zero_letters(letter)

    def is_empty(self):
        return len(self.__letters) == 0


def anagram_indicies(s, word):
    n = len(s)
    w = len(word)
    res = []

    if n < w:
        return res

    counter = LettersCounter()
    
    # add all letters from the original word
    for letter in word:
        counter.add_letter(letter)

    # remove first w letters from s string
    for i in range(w):
        counter.remove_letter(s[i])

    if counter.is_empty():
        res.append(0)
    
    for i in range(w, n):
        # continue with the same logic, add letters from front and remove from the current index
        counter.add_letter(s[i - w])
        counter.remove_letter(s[i])

        if counter.is_empty():
            # if there are 0 elements into dictionary, then the word is anagram
            res.append(i - w + 1)

    return res


###########
# Testing #
###########

# Correct result => [0, 3, 4]
print(anagram_indicies('abxaba', 'ab'))
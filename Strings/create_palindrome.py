'''
Create Palindrome

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. 
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

Input: 'race'
Output: 'ecarace'
Output explanation: Since we can add three letters to it (which is the smallest amount to make a palindrome). 
                    There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

Input: 'google'
Output: 'elgoogle'

=========================================
Solution explanation
	Time Complexity: 	O(N)    , The solution looks like O(N^2) but that's not possible
	Space Complexity: 	O(R)    , R = length of the new word (you need to the old string and allocate memory for that)
'''


############
# Solution #
############

def create_palindrome(string):
    n = len(string)

    # find the biggest left palindrome, which starts from the first letter
    max_left_palindrome = 1
    for i in reversed(range(1, n)):
        front = 0
        back = i
        found = True

        while front <= back:
            if string[front] != string[back]:
                found = False
                break
            front += 1
            back -= 1
        
        if found:
            max_left_palindrome = i + 1
            break

    # find the biggest right palindrome, which starts from the last letter
    max_right_palindrome = 1
    for i in range(n - 1):
        front = i
        back = n - 1
        found = True

        while front <= back:
            if string[front] != string[back]:
                found = False
                break
            front += 1
            back -= 1
        
        if found:
            max_right_palindrome = n - i
            break

    # reverse the string using [::-1]
    if max_right_palindrome > max_left_palindrome:
        return string + string[-max_right_palindrome - 1::-1]
    return string[:max_left_palindrome - 1:-1] + string


###########
# Testing #
###########

# Test 1
# correct result => 'ecarace'
print(create_palindrome('race'))

# Test 2
# correct result => 'elgoogle'
print(create_palindrome('google'))
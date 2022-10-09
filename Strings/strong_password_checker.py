'''
Strong Password Checker

A password is considered strong if the below conditions are all met:
- It has at least 6 characters and at most 20 characters.
- It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
- Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:
- Insert one character to password,
- Delete one character from password, or
- Replace one character of password with another character.

Input: password = "a"
Output: 5

Input: password = "aA1"
Output: 3

Input: password = "1337C0d3"
Output: 0

=========================================
Explanation in some kind of pseudo code:
if length < 6
    (3 different types characters, if all 5 are same, than 2 new separators should be added or 1 new added and 1 changed; or if all are the same type, 2 new types should be added, or 1 new and 1 changed)
    if length == 5 && (5 repeating or 1 char type)
        return 2
    return 6-length

if length > 20
    delete all till 20

*now you're in legnth > 5 && length <=20
    separate groups by changing a character (dividing all groups >=3 with 3)
    if char type 1 and changeChar here are <2
        changeChar += 2 - changeChar

return deletingChar + changeChar

first, make the string between 6 and 20 characters (when making this, separate/lower the groups bigger than 3)
    - when less than 6 characters Array.add((group+1)/2, 1, group/2) - ADDING CHARACTERS - or just use the upper logic when length < 3;
    - when more than 6 characters Array.add(group-1) - DELETING CHARACTERS, start from the one with groups bigger than 3, after that delete any)!!! Deleting priority 1. mod with 3 = 0 -> 2. mod with 3 = 1 -> 3. mod with 3 = 2

second, when the string is between 6 and 20 characters, change character in groups with same characters
3 -> 1 operation (*** -> *|*)   => 3/3 = 1
4 -> 1 operation (**** -> **|*) => 4/3 = 1
5 -> 1 operations (***** -> **|**)  => 5/3 = 1
6 -> 2 operations (****** -> **|*** -> **|**|)  => 6/3 = 2
7 -> 2 operations (******* -> **|**** -> **|**|*)   => 7/3 = 2
8 -> 2 operations (******** -> **|***** -> **|**|**)    => 8/3 = 2
9 -> 3 operations (********* -> **|****** -> **|**|**|) => 9/3 = 3
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

def strongPasswordChecker(password):
    groups = []
    length = len(password)
    last = 0
    lower = upper = digit = 0

    for curr in range(length):
        if password[curr].islower():
            lower = 1
        elif password[curr].isupper():
            upper = 1
        elif password[curr].isdigit():
            digit = 1

        if password[last] != password[curr]:
            groups.append(curr - last);
            last = curr

    groups.append(curr + 1 - last);
    lud = lower + upper + digit
    addSteps = 0

    # adding: under 6 chars
    if length < 6:
        if length == 5 and groups[0] == 5:
            addSteps = 2 # add + change, or add + add - it's same
        else:
            addSteps = 6 - length

        ludLeft = 3 - lud
        if addSteps < ludLeft:
            addSteps = ludLeft

        return addSteps

    # deleting: over 20 chars
    deleteSteps = 0
    groupsLength = len(groups)
    while length > 20:
        found = False

        for priority in range(3):
            for gidx in range(groupsLength):
                if groups[gidx] > 2 and groups[gidx] % 3 == priority:
                    groups[gidx] -= 1
                    found = True
                    break
            if found:
                break

        if not found:
            lastGroupIdx = groupsLength - 1
            groups[lastGroupIdx] -= 1
            if groups[lastGroupIdx] == 0:
                groups.pop(lastGroupIdx)
                groupsLength -= 1

        length -= 1
        deleteSteps += 1

    # changing: between 6 and 20 chars
    changeSteps = 0

    for gidx in range(groupsLength):
        changeSteps += groups[gidx] // 3

    ludLeft = 3 - lud
    if changeSteps < ludLeft:
        changeSteps = ludLeft

    return deleteSteps + changeSteps


###########
# Testing #
###########

# Test 1
# Correct result => 5
print(strongPasswordChecker('a'))

# Test 2
# Correct result => 3
print(strongPasswordChecker('aA1'))

# Test 3
# Correct result => 0
print(strongPasswordChecker('1337C0d3'))

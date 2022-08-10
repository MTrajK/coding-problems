# `5.2` **Find an Element Which is Smaller or Equal to Exactly K  Numbers**

## :pencil: Instructions:
You have to find some number X greater than 0 where exactly K elements in that list are greater than or equal to the number X.
If there are multiple such values return the smallest possible.
If there is no such X, return (-1).


### Expected Result:
```py
Input: [3,8,5,1,10,3,20,24], 2
Output: 11
Output explanation: Only 20 and 24 are greater or smaller from 11 (11 is the smallest solution, also 12, 13...20 are solutions).
```

## :bulb: Hint:
- Sort the array and check the Kth element from the end.
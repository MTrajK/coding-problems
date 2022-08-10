# `23` **Reverse Every Ascending Sublist**

## :pencil: Instructions:
Create and return a new list that contains the same elements as the argument list items, but
reversing the order of the elements inside every maximal strictly ascending sublist

### Expected Result:
```py
Input: [5, 7, 10, 4, 2, 7, 8, 1, 3]
Output: [10, 7, 5, 4, 8, 7, 2, 3, 1]
Output explanation: 5, 7, 10 => 10, 7, 5 ; 4 => 4; 2, 7, 8 => 8, 7, 2; 1, 3 => 3, 1
```

## :bulb: Hint:
Find the start and end of each sublist and reverse it in-place.

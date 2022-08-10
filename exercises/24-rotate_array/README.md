# `24` **Array rotation/shifting**

## :pencil: Instructions:
Rotate array in right (or left) for K places.

### Expected Result:
```py
Input: [1, 2, 3, 4, 5, 6], 1
Output: [6, 1, 2, 3, 4, 5]

Input: [1, 2, 3, 4, 5, 6], 3
Output: [4, 5, 6, 1, 2, 3]
```
## :bulb: Hint:
+ The first solution is a simple one, split the array in two parts and swap those parts.

+ For the second one we need to compute GCD, to decide how many different sets are there.
And after that shift all elements in that set for one position in right/left.
(elements in a set are not neighboring elements)

+ Try using a Juggling Algorithm

+ Link for Jugguling Algorithm:
https://www.geeksforgeeks.org/array-rotation/)
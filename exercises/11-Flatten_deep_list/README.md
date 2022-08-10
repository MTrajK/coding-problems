# `11` **Flatten an Arbitrarily Deep List**

## :pencil: Instructions:
Given a list that can contain arbitrary lists as its elements, which in turn can contain arbitrary lists
as elements, and so on, create and return a new list that contains all the atomic (that is, anything
that is not a list) elements listed in a linear sequence without any nesting.
### Expected Result:          

```py
Input: [1, [2, 3, [4, 'bob', 6], [7]], [8, 9]]
Output: [1, 2, 3, 4, 'bob', 6, 7, 8, 9]
```
## :bulb: Hint:

Recursive solution, extend the result with each sublist.
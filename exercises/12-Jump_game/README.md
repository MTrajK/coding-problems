# `12` **Jump Game**

## :pencil: Instructions:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

### Expected Result:          ```py
Input: [2, 3, 1, 1, 4]
Output: True

Input: [3, 2, 1, 0, 4]
Output: False
```

## :bulb: Hint:
Just iterate the array and in each step save the farthest reachable position.
If the current position is smaller than the farthest position, then the end isn't reachable.
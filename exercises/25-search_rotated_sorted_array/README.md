# `25` **Search in Rotated Sorted Array**

## :pencil: Instructions:

Suppose an `array` sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
You are given a target value to search. If found in the `array` return its index, otherwise return -1.
You may assume no duplicate exists in the `array`.

### Expected Result:
```py
Input: [4, 5, 6, 7, 0, 1, 2], 0
Output: 4

Input: [4, 5, 6, 7, 0, 1, 2], 3
Output: -1
```

## :bulb: Hint:
Use binary search twice, first time to find the pivot (index where the `array` is rotated)
and the second time to find the target.
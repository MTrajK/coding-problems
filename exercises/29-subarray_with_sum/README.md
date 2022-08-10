# `29` **Subarray with given sum**

## :pencil: Instrcutions:

Given an unsorted `array` A of size N of non-negative integers, find a continuous `sub-array`
which adds to a given number. Find starting and ending positions(1 indexing) of first such
occuring `subarray` from the left if sum equals to `subarray`, else print -1.

### Expected Result:

```py
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15
Output: 1, 5
```
## :Bulb: Hints:


+ Adjust the start and end index, in each step increase start or end idx.
+ If sum is bigger than K, remove element from the start idx from the sum.
+ Else add element from the end idx to the sum.
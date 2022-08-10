# **`08`Find Peak Element**

## :pencil: Instructions:
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

### Expected Result:          

```py
Input: [1, 2, 3, 1]
Output: 2
Output explanation: 3 is a peak element and your function should return the index number 2.

Input: [1, 2, 1, 3, 5, 6, 4]
Output: 1 or 5
Output explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```
## :bulb: Hint:
1. Look up Binary Search
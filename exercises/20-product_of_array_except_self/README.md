# `20` **Product of Array Except Self**
## :pencil: Instrcutions:

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
**Note:pencil::**  Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)



### Expected Result:          
```py
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

## :bulb: Hint:
2 iterations, one from front and the second from back.
Make the products as this: from 0 to i-1 and from i-1 to N-1, and in the end only multiply these 2 products.
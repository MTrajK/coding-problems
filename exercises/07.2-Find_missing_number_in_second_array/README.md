# `07.2` **Find missing number in second array**

## :pencil:Instructions:

All elements from the first array exist in the second array, except one. Find the missing number.

### Expected Result:         

```py
Sample input:   [1, 2, 3, 4, 5], [1, 2, 3, 4]
Sample output:  5

Sample input:   [2131, 2122221, 64565, 33333333, 994188129, 865342234],
                [994188129, 2122221, 865342234, 2131, 64565]
Sample output:  33333333
```

## :bulb:Hint:
Try to substract the sum of the second array from the sum of the first array:

### *Example:*

**missing_number = sum(arr1) - sum(arr2)**
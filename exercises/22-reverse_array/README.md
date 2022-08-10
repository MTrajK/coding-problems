# `22` **Reverse array**
## :pencil: Instructions: 
Reverse an array, in constant space and linear time complexity.

### Expected Result: 
```py
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## :bulb: Hint:
Reverse the whole array by swapping pair letters in-place (first with last, second with second from the end, etc).
Exist 2 more "Pythonic" ways of reversing arrays/strings (but not in-place, they're creating a new list):
>
```py
- reversed_arr = reversed(arr)
- reversed_arr = arr[::-1]
```
>
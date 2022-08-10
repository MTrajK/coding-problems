# `19` **Min Swapss**

## :pencil:Instrctions:

You have a list of numbers and you want to sort the list.
The only operation you have is a swap of any two arbitrary numbers.
Find the minimum number of swaps you need to do in order to make the list sorted (ascending order).

1. The array will contain N elements
2. Each element will be between 1 and N inclusive
3. All the numbers will be different

### Expected Result:          ```py
Input: [4, 1, 3, 2]
Output: 2
Output explanation: swap(4, 1) = [1, 4, 3, 2], swap(4, 2) = [1, 2, 3, 4]
```
## :bulb:Hint:

According to the description, all elements will have their position in the array,
for example, K should be located at K-1 in the array.
Itterate the array and check if each position has the right element,
if not, put that element in the right position and check again.
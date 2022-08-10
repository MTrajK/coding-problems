# `31` **Trapped Water**

## :pencil: Instrcutions:

You are given an `array` of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

### Expected Result:

```py

Input: [2, 1, 2]
Output: 1
Output explanation: We can hold 1 unit of water in the middle.

Input: [3, 0, 1, 3, 0, 5]
Output: 8
Output explanation: We can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
```

## :bulb: Hints:


+ The goal is to find the max wall and make 2 iterations starting from front and from back looking for the next bigger wall.

+ First search for the max wall from front, after that correct the left water starting from the back side.


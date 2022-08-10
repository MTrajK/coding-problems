# `28` **Sort RGB Array**


## :pencil: Instrcutions:

Given an `array` of strictly the characters 'R', 'G', and 'B', segregate
the values of the `array` so that all the Rs come first, the Gs come second, and the Bs come last.
You can only swap elements of the `array`.
Do this in linear time and in-place.

### Expected Result:

```py
Input: ['G', 'B', 'R', 'R', 'B', 'R', 'G']
Output: ['R', 'R', 'R', 'G', 'G', 'B', 'B']
```
## :Bulb: Hints:

+ Play with pointers/indices and swap elements. (only one iteration)

+ Save the last R, G and B indices, when adding some color, move the rest indices by 1.

+ Count R, G, B and populate the `array` after that. (2 iterations)

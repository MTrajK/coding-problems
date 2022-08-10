# `26` **Secret Santa**

## :pencil: Instrcutions:
Secret Santa is a game in which a group of friends or colleagues exchange Christmas presents anonymously,
each member of the group being assigned another member for whom to provide a small gift.
You're given a list of names, make a random pairs (each participant should have another name as pair).
Return an array with pairs represented as tuples.
### Expected Result:

```py
Input: ['a', 'b', 'c']
Output: This is a nondeterministic algorithm, more solutions exists, here are 2 possible solutions:
    [('a', 'b'), ('b', 'c'), ('c', 'a')], [('a', 'c'), ('c', 'b'), ('b', 'a')]
```

## :bulb: Hint:

Shuffle the `array` (this algorithm is explained in `shuffle_array.py`) and pair the current element
with the next element (neighbouring).
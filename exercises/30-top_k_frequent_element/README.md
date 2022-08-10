# `31` **Top K Frequent Elements**

## :pencil: Instrcutions:

+ Given a non-empty array of integers, return the k most frequent elements.
+ The order of the result isn't important.

### Expected Result:

```py
Input: [1, 1, 1, 2, 2, 3], 2
Output: [1, 2]

Input: [1], 1
Output: [1]
```
## :bulb: Hints:

+ Using Min Priority Queue, in each step add an element with its frequency and remove the element with the smallest frequency
if there are more than K elements inside the Priority Queue.

+ This solution isn't much faster than sorting the frequencies.

+ Using pivoting, this solution is based on the quick sort algorithm (divide and conquer).
Same pivoting solution as the nth_smallest.py.
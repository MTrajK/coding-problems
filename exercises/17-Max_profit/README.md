# `17` **Max Profit**

# :pencil: Instructions:
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

### Expected Result:          ```py
Input: [7, 1, 5, 3, 6, 4]
Output: 7
Output explanation: Buy on day 2 (price = 1) and sell on day 3  (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Input: [1, 2, 3, 4, 5]
Output: 4
Output explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
```

# :bulb: Hint:
Sum only the positive differences between neighbouring elements.
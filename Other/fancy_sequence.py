'''
Fancy Sequence

Write an API that generates fancy sequences using the append, addAll, and multAll operations.

Implement the Fancy class:
- Fancy() Initializes the object with an empty sequence.
- void append(val) Appends an integer val to the end of the sequence.
- void addAll(inc) Increments all existing values in the sequence by an integer inc.
- void multAll(m) Multiplies all existing values in the sequence by an integer m.
- int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.

Input: ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
Output: [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
Output explanation:
  Fancy fancy = new Fancy();
  fancy.append(2);   // fancy sequence: [2]
  fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
  fancy.append(7);   // fancy sequence: [5, 7]
  fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
  fancy.getIndex(0); // return 10
  fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
  fancy.append(10);  // fancy sequence: [13, 17, 10]
  fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
  fancy.getIndex(0); // return 26
  fancy.getIndex(1); // return 34
  fancy.getIndex(2); // return 20

=========================================
The program is meant to be called many times (more than a million), and because of that, each operation should be constant time.
When getIndex is called all we need to do is to take the first (getIndex index) adding+multiplying values and the last adding+multiplying values
and using these 2 values do math and determine the real adding+multlplying values.
When there is a new adding value, just increase the adding value with that one.
When there is a new multiplying value, multiply the both adding and multiplying values.
Example x=append(8): (((x + 5) + 6) + 7) * 2 = (x + 17) * 2 = x * 2 + 34
So total multiplayer is 2.
And total adder is 18 (from 36/2).
The result is (8+18)*2 = 52.
Example y=append(9) after addAll(6) operation:
(y + 7) * 2 = y * 2 + 14
The total multiplayer is the same, 2 (the previous is 1, the last is 2 that's equal to 2/1=2).
But the total adder is 7, the total last adder is 18 (from 36/2) minus the previous 11 (from 5+6 with no multiplyers till that moment).
The result is (9+7)*2 = 32.
    Time Complexity (The whole program, N operations):    O(N)
    Time Complexity (Only one operation): O(1)
    Space Complexity:   O(N)
'''

############
# Solution #
############

class Fancy:
    def __init__(self):
        self.appending = []
        self.adding = []
        self.multiplying = []


    def append(self, val: int) -> None:
        self.appending.append(val)

        if len(self.appending) > 1:
            self.adding.append(self.adding[-1])
            self.multiplying.append(self.multiplying[-1])
        else:
            self.adding.append(0)
            self.multiplying.append(1)

    def addAll(self, inc: int) -> None:
        if len(self.appending) == 0:
            return

        self.adding[-1] += inc


    def multAll(self, m: int) -> None:
        if len(self.appending) == 0:
            return

        self.adding[-1] *= m
        self.multiplying[-1] *= m


    def getIndex(self, idx: int) -> int:
        length = len(self.appending)
        if idx >= length:
            return -1

        prevAdding = 0
        prevMultiplying = 1
        if idx > 0:
            prevMultiplying = self.multiplying[idx-1]
            prevAdding = self.adding[idx-1]

        currMultiplying = self.multiplying[-1] // prevMultiplying
        currAdding = self.adding[-1] - (prevAdding * currMultiplying)

        return (self.appending[idx] * currMultiplying + currAdding) % 1000000007


###########
# Testing #
###########

# Test 1
fancy = Fancy()
fancy.append(2)           # fancy sequence: [2]
fancy.addAll(3)           # fancy sequence: [2+3] -> [5]
fancy.append(7)           # fancy sequence: [5, 7]
fancy.multAll(2)          # fancy sequence: [5*2, 7*2] -> [10, 14]
print(fancy.getIndex(0))  # return 10
fancy.addAll(3)           # fancy sequence: [10+3, 14+3] -> [13, 17]
fancy.append(10)          # fancy sequence: [13, 17, 10]
fancy.multAll(2)          # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0))  # return 26
print(fancy.getIndex(1))  # return 34
print(fancy.getIndex(2))  # return 20

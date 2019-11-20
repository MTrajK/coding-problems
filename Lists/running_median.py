'''
Running Median

Compute the running median of a sequence of numbers. 
That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.

Input: [2, 1, 5, 7, 2, 0, 5]
Output:
2
1.5
2
3.5
2
2
2

=========================================
Using 2 heaps (priority queues) balance the left and right side of the stream.
    Time Complexity:    O(N LogN)
    Space Complexity:   O(N)
'''


############
# Solution #
############

from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self, isMin=True):
        self.data = []
        self.isMin = isMin

    def push(self, el):
        if not self.isMin:
            el = -el
        heappush(self.data, el)

    def pop(self):
        el = heappop(self.data)
        if not self.isMin:
            el = -el
        return el

    def peek(self):
        el = self.data[0]
        if not self.isMin:
            el = -el
        return el

    def count(self):
        return len(self.data)

def running_median(stream):
    left_heap = PriorityQueue(False)
    right_heap = PriorityQueue()

    # left_heap will have always same number of elements or 1 element more than right_heap
    for number in stream:
        if left_heap.count() == 0:
            # enters here only for the first element of the streen
            left_heap.push(number)
        # balance the heaps
        elif left_heap.count() > right_heap.count():
            # in this case the right_heap should get a new element (so both heaps will have same number of elements)
            if left_heap.peek() > number:
                # move an element from left to right heap
                right_heap.push(left_heap.pop())
                left_heap.push(number)
            else:
                right_heap.push(number)
        else:
            # in this case the left_heap should get a new element (so the left_heap will have 1 more element)
            if right_heap.peek() < number:
                # move an element from right to left heap
                left_heap.push(right_heap.pop())
                right_heap.push(number)
            else:
                left_heap.push(number)

        if left_heap.count() > right_heap.count():
            # if left_heap is bigger then odd elements from the stream are processed
            # because left_heap is bigger ONLY BY 1 element from right_heap (n + n + 1 = 2n + 1)
            print(left_heap.peek())
        else:
            # both heaps have same length, so the count from the elements is even (n + n = 2n)
            print((left_heap.peek() + right_heap.peek())/2)


###########
# Testing #
###########

# Test 1
# Correct result => 2 1.5 2 3.5 2 2 2
running_median([2, 1, 5, 7, 2, 0, 5])
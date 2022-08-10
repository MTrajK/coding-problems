import heapq

# priority queue comparator class
# acctualy in this case you don't need a comparator class, because the elements are tuples
# and comparison operator can work with tuples
# (The comparison starts with a first element of each tuple. If they do not compare to =,< or > then it proceed to the second element and so on.)
class PQElement:
    def __init__(self, el):
        self.frequency, self.val = el

    def __lt__(self, other):
        return self.frequency < other.frequency

# priority queue
class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, el):
        heapq.heappush(self.data, PQElement(el))

    def pop(self):
        return heapq.heappop(self.data)

    def count(self):
        return len(self.data)

def top_k_frequent_1(nums, k):
    frequency = {}

    # count the frequency of each unique element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    arr = [(frequency[el], el) for el in frequency]
    n = len(arr)

    if k > n:
        return [el[1] for el in arr]
    if k < 1:
        return []

    heap = PriorityQueue()
    for el in arr:
        # push all elements
        heap.push(el)
        # pop the element with smallest frequency
        if heap.count() > k:
            heap.pop()

    # take all elements from the heap
    # no need from K times heap.pop() (K LogK), because we already have the array with data (K)
    return [el.val for el in heap.data]


##############
# Solution 2 #
##############

def top_k_frequent_2(nums, k):
    frequency = {}

    # count the frequency of each unique element
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    arr = [(frequency[el], el) for el in frequency]
    n = len(arr)

    if k > n:
        return [el[1] for el in arr]
    if k < 1:
        return []

    # pivoting, find the first k elements with the biggest frequency, O(U), U = num of unique nums
    k -= 1
    left = 0
    right = n - 1

    while True:
        pivot = pivoting(arr, left, right)

        if pivot > k:
            right = pivot - 1
        elif pivot < k:
            left = pivot + 1
        else:
            return [el[1] for el in arr[:k + 1]]

    # not possible
    return None

def pivoting(arr, left, right):
    # Linear time complexity pivoting
    # takes the last element as pivot
    pivot = right
    new_pivot = left

    # iterate the whole array (without the last element)
    # and put all elements bigger than the pivot (last element) in the first K spots
    # with the new_pivot we're "counting" how many bigger elements are there
    for j in range(left, right):
        if arr[j][0] > arr[pivot][0]:
            swap(arr, new_pivot, j)
            new_pivot += 1

    # swap the last (pivot) element with the new_pivot position
    swap(arr, new_pivot, pivot)

    # return the new pivot
    return new_pivot

def swap(arr, i, j):
    # swaps two elements in an array
    arr[i], arr[j] = arr[j], arr[i]
def sort_rgb_array(arr):
    n = len(arr)

    # indexes/pointers of the last element of each color
    r, g, b = 0, 0, 0

    for i in range(n):
        # swap the element and move the pointer
        if arr[i] == 'R':
            swap(arr, i, r)
            r += 1

        # move pointer
        if r > g:
            g = r

        # swap the element and move the pointer
        if arr[i] == 'G':
            swap(arr, i, g)
            g += 1

        # move pointer
        if g > b:
            b = g

        # swap the element and move the pointer
        if arr[i] == 'B':
            swap(arr, i, b)
            b += 1

    return arr

def swap(arr, i, j):
    # swaps two elements in an array
    arr[i], arr[j] = arr[j], arr[i]


##############
# Solution 2 #
##############

def sort_rgb_array_2(arr):
    rgb = {
        'R': 0,
        'G': 0,
        'B': 0
    }

    # count colors
    for c in arr:
        rgb[c] += 1

    # adjust the intervals
    rgb['G'] += rgb['R']
    rgb['B'] += rgb['G']

    # assign colors
    for i in range(len(arr)):
        if i < rgb['R']:
            arr[i] = 'R'
        elif i < rgb['G']:
            arr[i] = 'G'
        else:
            arr[i] = 'B'

    return arr
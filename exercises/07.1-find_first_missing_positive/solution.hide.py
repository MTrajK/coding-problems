##############
# Solution 1 #
##############

def find_first_missing_1(a):
    n = len(a)

    for i in range(n):
        while (a[i] > 0) and (a[i] <= n):
            swap = a[i] - 1
            if a[i] == a[swap]:
                break

            # swap elements
            a[i], a[swap] = a[swap], a[i]

    for i in range(n):
        if a[i] - 1 != i:
            return i + 1

    return n + 1
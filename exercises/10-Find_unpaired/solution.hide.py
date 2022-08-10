def find_unpaired_element(arr):
    unique = 0

    for el in arr:
        unique ^= el

    return unique
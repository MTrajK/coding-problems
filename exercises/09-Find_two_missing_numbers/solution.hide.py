def missing_numbers(nums):
    # find sums from the array
    s = 0
    s_2 = 0
    for i in nums:
        s += i
        s_2 += i * i

    n = len(nums) + 2

    # using formulas, compute the sums of the sequence
    f_s = n * (n + 1) // 2
    f_s_2 = n * (n + 1) * (2 * n + 1) // 6

    # difference of sums
    d = f_s - s
    d_2 = f_s_2 - s_2

    # using quadratic formula find the values
    r = int(math.sqrt(2 * d_2 - d * d))

    a = (d - r) // 2
    b = (d + r) // 2

    return [a, b]
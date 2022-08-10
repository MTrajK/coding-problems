def product_except_self(nums):
    n = len(nums)
    if n == 0:
        return []

    mult = 1
    res = [1]
    i = 0

    # all products from right to left
    while i < n - 1:
        mult *= nums[i]
        res.append(mult)
        i += 1

    mult = 1
    i = n - 2

    # all products from left to right
    while i >= 0:
        mult *= nums[i + 1]
        res[i] *= mult
        i -= 1

    return res
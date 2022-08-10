def missing_number(nums):
    s = sum(nums)
    n = len(nums) + 1
    # sum formula (sum of the first n numbers) = (N*(N+1))/2
    return n * (n + 1) // 2 - s
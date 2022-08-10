def find_peak_element(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            # go left if the current value is smaller than the next one
            # in this moment you're sure that there is a peak element left from this one
            r = mid
        else:
            # go right if the current value is smaller than the next one
            # if the l comes to the end and all elements were in ascending order, then the last one is peak (because nums[n] is negative infinity)
            l = mid + 1

    return l
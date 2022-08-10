
def search_rotated_sorted_array(nums, target):
    n = len(nums)
    pivot = find_pivot(nums, 0, n) + 1
    if pivot > n:
        return -1

    if nums[0] <= target:
        return find_element(nums, 0, pivot - 1, target)
    return find_element(nums, pivot, n - 1, target)

def find_pivot(nums, left, right):
    while left < right - 1:
        mid = left + (right - left) // 2

        if nums[left] < nums[mid]:
            left = mid
        else:
            right = mid

    return left

def find_element(nums, left, right, target):
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
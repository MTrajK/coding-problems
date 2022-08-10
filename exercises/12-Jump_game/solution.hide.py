
def can_jump(nums):
    n = len(nums)
    if n == 0:
        return False

    max_jump = 0
    for i in range(n):
        # if this field isn't reachable return False
        if max_jump < i:
            return False

        this_jump = i + nums[i]
        max_jump = max(max_jump, this_jump)

        # if the jump is greater or equal to the last element return True
        if max_jump >= n - 1:
            return True
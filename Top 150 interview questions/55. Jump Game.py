class Solution(object):
    def canJump(self, nums):
        curr = nums[0]
        for i in range(1,len(nums)):
            if curr == 0:
                return False
            curr -= 1
            curr = max(curr, nums[i])     
        return True

"""
The overall idea here is that if the first element of the array is 0 we can't jump to any other array and it will directly return False.
It keeps track of the maximum number of steps that can be taken from the current position using the curr variable.
"""

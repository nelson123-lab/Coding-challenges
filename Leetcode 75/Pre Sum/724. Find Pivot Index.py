class Solution:
    def pivotIndex(self, nums) -> int:
        leftSum = rightSum = 0
        i = 0
        leftSum = sum(nums[:i])
        rightSum = sum(nums[i+1:])
        if leftSum == rightSum:
            return 0
        for i in range(1, len(nums)):
            """
            [1,7,3,6,5,6]
               ^
            When index starts from 1. we add i-1 that is nums[0] to leftSum and substract nums[1] from rightSum.
            """
            leftSum += nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            else: pass
        return -1
    
a = Solution()
print(a.pivotIndex([1,7,3,6,5,6]))

"""
Using the principle of sliding window to reduce the complextiy of the algorithm. Instead of checking the leftSum and rightSum for each index we can 
add and substract the elements from the previous index to the leftSum and the substract the current index value from the rightSum.
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left = 0
        for i , num in enumerate(nums):
            if left == total -left - num:
                return i
            left += num
        return -1

"""
Here the left sum is compared with the total sum each time to find the index of pivot.
Time Complexity O(n)
Space Complexity O(1)
"""

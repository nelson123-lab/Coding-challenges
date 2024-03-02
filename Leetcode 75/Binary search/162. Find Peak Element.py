class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        nums = [0] + nums + [0]
        for no in range(1, len(nums)-1):
            if nums[no-1] < nums[no] and nums[no+1] < nums[no]:
                return no-1
            else: pass
        return 0
"""
This solution uses the principle of adding one zero element in the starting and the end of the list. But it works in O(n) time complexity hence not an optimized solution
Time Complexity O(n)
Space Complexity O(n) since we are adding 0 to the nums list which creates a copy of the list.
"""

# Solution using Binary search
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) -1
        while l <= r:
            mid = l + ((r-l)//2)

            # left greater
            if mid > 0 and nums[mid] < nums[mid -1]:
                r = mid -1

            # right greater
            elif mid < len(nums)-1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else: 
                return mid

"""
Here we are using a binary search operation to check which side of the mid is the peak. The binary search directs towards the greater neighbor of the mid.
Time COmplexity O(logn)
Space Complexity O(1)
"""

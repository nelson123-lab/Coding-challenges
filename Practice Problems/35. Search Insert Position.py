class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        nearest_index = 0
        while l<r:
            mid = r-l//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                nearest_index = mid
            else: 
                l = mid + 1
                nearest_index = mid
        return nearest_index
            
            
"""
Here we need to do a binary search to find the target and run the algorithm in O(logn) complexity.
"""

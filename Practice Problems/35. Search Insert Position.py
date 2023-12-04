class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # Checking the edge conditions.
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0

        # We start with the binary search.
        else:
            while l<=r:
                mid = r+l//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else: 
                    l = mid + 1

        # This is the part of the code that finds the position of the number to be if it is not found.
        if target < nums[r]:
            return l
        else:
            return r + 1
            
            
"""
Here we need to do a binary search to find the target and run the algorithm in O(logn) complexity.
Time Complexity O(logn)
Space Complexity O(1)
"""

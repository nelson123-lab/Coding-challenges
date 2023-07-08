class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left  = right = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left
"""
Here it is the similar to the problem Max Consecutive one by removing k values. Here the k is 1. 
The algorithm first checks for 0 and if it is a 0 k value reduces and if it is less than 0. Which means there have been more than one 0 so we need to check
other subarray. 
The pointer left checks from the left again whether the elements are 1 or 0 and increases tha value of k when it is 0. 
"""

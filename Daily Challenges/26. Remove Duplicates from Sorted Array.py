class Solution(object):
    def removeDuplicates(self, nums):
        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1   
                nums[k] = nums[i]
        return k+1

"""
Time Complexity O(n)
Space Complexity O(n)
"""

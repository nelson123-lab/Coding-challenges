class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]:
                nums[i] = nums[j]
                i += 1
        del nums[i:]
        return len(nums)
"""
Here two pointers i and j are used used to iterate through the list and whenever values at index j not index at i-1 we replace the value at
index i with j and increase the i value.
"""

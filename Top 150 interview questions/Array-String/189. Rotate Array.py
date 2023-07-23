class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
"""
This is the easiest way to rotate the array using the slicing the array into two parts and combining it together. 
nums[:] means the entire array.
nums[-k:] means starting from -k to end.
nums[:-k] means from start to -k.
"""

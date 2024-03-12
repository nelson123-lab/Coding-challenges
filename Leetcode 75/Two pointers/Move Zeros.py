class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return nums

"""
The solution uses two pointer approach where j keep track of the zeros and 
i is used to iterate over the list. 
Each time a non zero number is swapped places with a zero so that in O(n) time complexity
we are able to find the solution.

"""
ans = Solution()
print(ans.moveZeroes([0,1,0,3,0,0,12]))

# Approach 2 similar to 1 but more understandable.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, non_zero = 0, 0
        while non_zero < len(nums):
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
                non_zero += 1
                zero += 1
            else: 
                non_zero += 1
        return nums

"""
Time Complexity O(n)
Space Complexity O(1)
"""

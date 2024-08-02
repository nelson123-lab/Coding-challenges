# Brute force approach
class Solution:
    def product(self, arr):
        res = 1
        for no in arr:
            res *= no
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = [1]*len(nums)
        while i < len(nums):
            res[i] = self.product(nums[:i]  + nums[i+1:])
            i += 1
        return res

"""
- Here we are first writing a function to find the product of the array.
- We are then using the sliding window approach so each time we are iterating through the list, we combine the left and right sides of the array, find the product, and store the value in the output array.

Time COmplexity O(n^2)
Space Compleixity O(n)
"""

# Optimal solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
"""
Reference: watch this video : https://youtu.be/bNvIQI2wAjk
- Here we use the prefix and the postfix approach to find the product of the array except self.

Time Complexity O(n)
Space Complexity O(n)
"""

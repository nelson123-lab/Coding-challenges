class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def arrayProduct(lst):
            out = 1
            for i in lst:
                out = out * i
            return out

        res = [0]* len(nums)
        for i in range(len(nums)):
            cur_ele = nums[i]
            remaining_element = nums[:i] + nums[i+1:]
            res[i] = arrayProduct(remaining_element)
        return res

"""
This is an O(n*2) approach to solve this problem but it fails due to time limit error.
"""



class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        result = [1]*length
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(length-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
    
a = Solution()
print(a.productExceptSelf([1,2,3,4]))

"""
Time Complexity O(n)
Space COmplexity O(n)
"""

# Explanation video in youtube
# https://youtu.be/bNvIQI2wAjk

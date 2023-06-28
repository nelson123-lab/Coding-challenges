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
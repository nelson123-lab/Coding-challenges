class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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

"""
Since we are not able to use the "/" operator. It becomes harder to do this problem in O(n) time complexity. 
This solution works in O(n) since there are no nested for loops.
There is trick you need to know inorder to solve this problem.
Reference:-

"""

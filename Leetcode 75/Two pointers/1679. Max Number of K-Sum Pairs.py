class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        output = 0
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum == k:
                output += 1
                left += 1
                right -= 1
            elif currSum < k:
                left += 1
            else:
                right -= 1
        return output

"""
- Here we are using two pointer to keep track of left and right pointers to check if the sum is equal to the K.
- Whenever there is a sum which is equal to k the left pointer should be increased and right pointer should be decreased.
Time COmplexity O(nlogn)
Space Complexity O(1)
"""

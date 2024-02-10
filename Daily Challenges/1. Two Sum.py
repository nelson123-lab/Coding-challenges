class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        length = len(nums)
        for i in range(length):
            diff = target - nums[i]
            if diff not in dic:
                dic[nums[i]] = i
            else:
                return [dic[diff], i]
"""
TIme Compelxity O(n)
Space Complexity O(n)
"""

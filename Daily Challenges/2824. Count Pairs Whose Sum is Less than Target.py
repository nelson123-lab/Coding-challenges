class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        i = 0
        while i < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    pairs += 1
                else: pass
            i += 1
        return pairs


"""
Time Complexity O(n^2)
Space Complexity O(n)
"""


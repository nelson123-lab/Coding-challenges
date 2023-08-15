class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for  idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in res and res[diff] != idx:
                return res[diff], idx
            else:
                res[nums[idx]] = idx
        return []
"""
Time Complexity O(n)
- We are iterating through the loop one time.
Space Complexity O(n)
- We use n space according to the input in the worst case for the hashmap.
"""

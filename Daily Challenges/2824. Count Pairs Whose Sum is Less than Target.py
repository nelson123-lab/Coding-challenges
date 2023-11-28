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

"""
Here we can even use the two pointer approach since we only need to know whether two pairs are less than the target we don't need to know what are the indices of the pairs.
"""

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        no_pairs = 0
        while l < r:
            if nums[l] + nums[r] < target:
                no_pairs += (r - l) # This means if the above statement is true then all the values in between the r and l will be true.
                l += 1
            else: r -= 1
        return no_pairs

"""
Time complexity O(nlogn)
Space Complexity O(n)
"""

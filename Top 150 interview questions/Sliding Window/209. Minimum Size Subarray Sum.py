class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total_sum = 0, 0
        res = float('inf')

        for right in range(len(nums)):
            total_sum += nums[right]

            while total_sum >= target:
                res = min(right-left + 1, res)
                total_sum -= nums[left]
                left += 1
        return 0 if res == float('inf') else res
                
"""
- Here 2 pointers act as the start and end of the sliding window. The values are added to the total sum each time and compares with the target. 
- When the total sum is less than target we add the next element else we substracts the starting element of the sliding window and checks again.
Time Complexity O(n)
Space Complexity O(1)
"""

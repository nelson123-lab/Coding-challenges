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
                

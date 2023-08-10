class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        min_len = 0
        curr_sum = 0
        s_i, s_e = 0, 0

        for window_end in range(len(nums)):
            curr_sum += nums[window_end]

            while curr_sum > target

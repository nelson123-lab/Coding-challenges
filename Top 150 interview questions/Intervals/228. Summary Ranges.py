class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        numset = set(nums)
        idx, start, curr_end = 0, 0, 0
        res = []
        while idx < len(nums):
            if nums[idx] -1 not in numset:
                curr_end = nums[idx]
                start = nums[idx]
            while nums[idx] + 1 in numset:
                curr_end += 1
                idx += 1
            if start == curr_end:
                res.append(str(start))
            else:
                res.append(f"{start}->{curr_end}")
            idx += 1
        return res
"""
Time Complexity O(n)
- Here we iterate through the input array
Space Complexity O(1)
- Here even though we use a list ot store the output, it doesn't add to the space complexity of the algorithm. It's because the problem statement wants the output to be like that. We could return 
one at a time without storing it in a list and returning it together.
"""

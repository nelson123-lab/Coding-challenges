class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                curr_length = 1
                while (n + curr_length) in numSet:
                    curr_length += 1 #4
                longest = max(curr_length, longest)
        return longest # 4

"""
- Here we are creating a num set to keep track of the elements.
- We are finding all the sequeences length present in the list and then finds the max length as the longest.

Time Compelxity O(n)
Space COmplexity O(n)
"""

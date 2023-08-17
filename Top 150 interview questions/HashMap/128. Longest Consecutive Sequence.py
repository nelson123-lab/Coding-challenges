"""
We cannot sort the array to find the longest consecutive list of numbers. It is required that the time complexity should be O(n). The sorting makes it O(nlogn) time complexity itself.
"""

"""
This is a solution with sorting.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Checking if the length is 0, then there is no consecutive elements.
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        max_seq, curr_max = 1, 1
        # The list contains duplicates as well we need to get rid of that. 
        nums = list(set(nums))
        # Sorting it to check the longest consecutive numbers.
        nums.sort()
        # The start and end should be initialized after the making the modification of the lists. Since converting the list to set reduces the number of elements.
        # If this is initialized before modification it will result in index out of the range error.
        start, end = 0, len(nums)
        while start < (end - 1): # end -1 to avoid the index out of the range error.

            if nums[start + 1] - nums[start] == 1:
                curr_max += 1
            else:
                curr_max = 1
            # we need to increase the start value so that iteration should happen.
            start += 1
            if curr_max > max_seq:
                max_seq = curr_max
        return max_seq
"""
Time Complexity O(nlogn)
- Here the worst complexity is O(n log n) since sorting is done.
Space Complexity O(n)
- A set is used to store the eleements which results in O(n) space complexity.
"""

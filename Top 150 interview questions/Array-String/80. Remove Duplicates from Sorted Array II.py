class Solution:
    def removeDuplicates(self, nums) -> int:
        ele = nums[0]
        count = 0
        k = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == ele:
                count += 1
                if count > 2:
                    nums[i] = float('inf')
                    k += 1
            else:
                count = 1
                ele = nums[i]
        nums.sort()
        return length - k
"""
Here a count is initialized to check whether a number is repeated more than twice. If it is repeated it will be replaced by float('inf').
This makes it easier to be sorted out.
"""

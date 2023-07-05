class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

nums = [20,100,10,12,5,13]
a = Solution()
print(a.increasingTriplet(nums))
"""
This soulution fails to meet the i<j<k but returns 3 numbers that meets nums[i]< nums[j] < nums[k].
"""

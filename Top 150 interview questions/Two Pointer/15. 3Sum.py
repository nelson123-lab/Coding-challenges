class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] == -nums[k]:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res

"""
Time Complexity O(n^2)
- Here the while loop is iterating inside the for loop which results in this time complexity.
Space Complexity O(n)
- Here a set is used to store the information which can be upto the input size.
"""

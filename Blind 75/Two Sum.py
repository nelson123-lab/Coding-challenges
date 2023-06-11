# To find the indexes of two elements that add up to the target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterating through the number list.
        for i in range(len(nums)):
          """
          Finding the difference between each elements and the target inorder to check whether 
          the difference exists within the list and return the indices of the both.
          """
            a = target - nums[i]
            if a in nums and nums.index(a) != i:
                return [i, nums.index(a)]
            else:
                pass

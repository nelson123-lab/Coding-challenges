class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even, odd = 0, 1
        res = [0]* len(nums)
        for k in range(len(nums)):
            if nums[k] > 0:
                res[even] = nums[k]
                even += 2
            else:
                res[odd] = nums[k]
                odd += 2
        return res

  """

  - Here the solution uses Two pointer even and odd to keep track of the positive and negative numbers. All the positive numbers are present in the even positions according to the index(0,2,4,6) and all the negative values are
  present in the odd positions (1,3,5,7). 
  - We are then using a pointer k to keep track of each of the elements within the nums and adding the positive and negative numbers each time to the res list.
  Time Complexity O(n)
  Space Compelexity O(n)
  """

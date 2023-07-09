class Solution:
    def findDifference(self, nums1, nums2):
        nums, nums2 = list(set(nums1)), list(set(nums2))
      """
      Making a copy of the list. When elements of a list are removed while iteration it will result in not iterating through all the elements.
      """
        a = nums.copy()
        for i in nums:
            if i in nums2:
                nums2.remove(i)
                a.remove(i)
            else: pass
        return [a, nums2]

# The same results can be obtained by using set operations
class Solution:
    def findDifference(self, nums1, nums2):
        nums1, nums2 = set(nums1), set(nums2)
        return [list(nums1-nums2), list(nums2-nums1)]

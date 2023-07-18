class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        return nums1.sort()

"""
Assigning the values of nums2 into nums1 after the elements in the nums1.

Similar results can be obtained by iterating through nums1 and updating the values nums1.

for i in range(m,m+n):
    nums1[i]=nums2[i-m]
"""

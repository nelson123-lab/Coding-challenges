class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        A, B = set(nums1), set(nums2)

        return [list(A-B), list(B-A)]
        
"""
This is a quesiton using sets. We are converting the sets in A and B and finding the differnce using the set methods.
Time complexity O(n)
Space Complexity O(n)
where n = n1 + n2
"""

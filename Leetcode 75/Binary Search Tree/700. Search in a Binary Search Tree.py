# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        curr_n = root
        while curr_n:
            if curr_n.val == val:
                return curr_n
            elif val > curr_n.val:
                curr_n = curr_n.right
            else:
                curr_n = curr_n.left
        return None

"""
- Here we are using the property of a binary search tree. The values to the left and left of the root will always be lesser than the root, and the values to the right are always greater.
- We are comparing the current node value with the value that we need to search each time similar to a binary search and points our direction to left or right.

Time Complexity O(n)
Space Complexity O(1)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
- Here we are using a recursive approach to find the depth of the binary tree.
- we are finding the max depth of the right and left sub-tree each time to find the total depth of the binary tree.
- The same problem can be solved in iterative and BFS as well.
"""

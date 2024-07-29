# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Checking if the root node exist.
        if not root:
            return None
        # Swapping the values of the child nodes each time.
        root.left, root.right = root.right, root.left
        # Doing recursive call.
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

"""
- Here when we visit each node we are swapping the values of its children. ie, left and right will be swapped.
- We are using a DFS it doesn't matter if it's pre or post-order.
"""

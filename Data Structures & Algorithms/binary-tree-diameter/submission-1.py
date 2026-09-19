# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx = 0

        def maxDepth(root):
            nonlocal mx

            if not root:
                return 0

            left = maxDepth(root.left)
            right = maxDepth(root.right)

            # Diameter passing through this node
            mx = max(mx, left + right)

            # Return height to the parent
            return 1 + max(left, right)

        maxDepth(root)

        return mx
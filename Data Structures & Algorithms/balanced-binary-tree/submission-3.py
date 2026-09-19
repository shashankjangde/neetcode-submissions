# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(root):
    if not root:
        return 0

    left = check(root.left)
    right = check(root.right)

    # If either subtree is already unbalanced
    if left == -1 or right == -1:
        return -1

    # If current node is unbalanced
    if abs(left - right) > 1:
        return -1

    # Return height of current subtree
    return max(left, right) + 1


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check(root) != -1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
           
        if not root.left or not root.right:
            return 1
        
        left = 1+self.maxDepth(root.left)
        right = 1+self.maxDepth(root.right)

        return max(left,right)
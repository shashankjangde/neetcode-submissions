from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        nodes = set()
        while q:
            cur = q.popleft()
            if cur:
                nodes.add(cur)

            if cur and cur.left:
                q.append(cur.left)
            
            if cur and cur.right:
                q.append(cur.right)
            
        
        for i in nodes:
            i.left, i.right = i.right, i.left
        
        return root


            


        
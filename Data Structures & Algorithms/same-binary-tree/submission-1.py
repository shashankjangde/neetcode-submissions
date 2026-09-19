# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur1 = p
        cur2 = q
        d1 = deque([cur1])
        d2 = deque([cur2])

        while d1 and d2:
            cur1 = d1.popleft()
            cur2 = d2.popleft()
            if cur1 == None and cur2 == None:
                continue
            elif cur1 == None or cur2==None:
                return False
            elif cur1.val != cur2.val:
                return False
            else:
                d1.append(cur1.left)
                d1.append(cur1.right)
                d2.append(cur2.left)
                d2.append(cur2.right)
            
        return True

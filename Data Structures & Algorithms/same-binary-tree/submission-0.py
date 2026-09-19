# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1 = []
        s2 = []

        cur = p

        dq = deque([cur])
        while dq:
            cur = dq.popleft()
            if cur!=None:
                s1.append(cur.val)
                dq.append(cur.left)
                dq.append(cur.right)
            else:
                s1.append(None)

        cur = q
        dq = deque([cur])
        while dq:
            cur = dq.popleft()
            if cur != None:
                s2.append(cur.val)
                dq.append(cur.left)
                dq.append(cur.right)
            else:
                s2.append(None)

        return s1==s2


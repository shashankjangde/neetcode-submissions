# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        new = []
        n = len(vals)
        odd = False
        for i in range(n):
            if odd:
                new.append(vals[n-(ceil(i/2))])
                odd = False
            else:
                new.append(vals[i//2])
                odd = True
        
        cur = head
        i = 0
        while cur:
            cur.val = new[i]
            cur = cur.next
            i+=1


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
            vals.append(cur)
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
        
        cur = new[0]
        i=0
        while i<len(new)-1:
            cur.next = new[i+1]
            cur = new[i+1]
            i+=1
        cur.next = None



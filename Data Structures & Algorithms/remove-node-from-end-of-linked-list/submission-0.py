# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        l = 0
        cur = head
        while cur:
            l+=1
            cur = cur.next

        i = 0
        n = n%l
        prev = None
        cur = head
        while i<n:
            prev = cur
            cur = cur.next
            i += 1
        prev.next = cur.next
        return head

        
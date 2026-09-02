# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseLL(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        head = reverseLL(head)

        i = 1

        if n == 1:
            head = head.next
            return head
        
        prev = None
        cur = head
        while i<n:
            i += 1
            prev = cur
            cur = cur.next
        prev.next = cur.next

        head = reverseLL(head)

        return head
        
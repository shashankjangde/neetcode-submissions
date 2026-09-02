# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLL(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        temp = reverseLL(temp)

        odd = False
        cur = head
        nxt = temp
        while cur:
            if odd:
                nxt = cur.next
                cur.next = temp
                odd = False
            else:
                temp = cur.next
                cur.next = nxt
                odd = True
            cur = cur.next
                



        

        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        i = 1
        cur = dummy.next
        prev = dummy
        cur_head = dummy.next
        tail = None

        while cur:
            if i == k:
                temp = cur.next
                cur.next = None
                reverse(cur_head)
                prev.next = cur
                cur_head.next = temp
                i=0
                prev = cur_head
                cur = cur_head
                cur_head = temp
            i+=1
            cur = cur.next
        return dummy.next

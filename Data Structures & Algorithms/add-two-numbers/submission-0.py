# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_head = ListNode(-1, ListNode(0))

        d1 = l1
        d2 = l2
        cur = new_head

        while d1 and d2:
            cur.next = ListNode(0)
            cur = cur.next
            val = d1.val+d2.val+carry
            cur.val = val%10
            carry = val//10

            d1 = d1.next
            d2 = d2.next
        
        while d1:
            cur.next = ListNode(0)
            cur = cur.next
            val = d1.val + carry
            cur.val = val%10
            carry = val//10

        while d2:
            cur.next = ListNode(0)
            cur = cur.next
            val = d2.val + carry
            cur.val = val%10
            carry = val//10
        
        if carry == 1:
            cur.next = ListNode(1)

        return new_head.next
        

        
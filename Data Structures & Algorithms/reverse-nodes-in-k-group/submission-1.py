# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse current group
            prev = group_next
            cur = group_prev.next

            while cur != group_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # Reconnect reversed group
            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start
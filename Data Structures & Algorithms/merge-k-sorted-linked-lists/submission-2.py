# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(head1: Optional[ListNode],head2: Optional[ListNode]) -> Optional[ListNode]:
    left, right = head1, head2
    newhead = ListNode(-10001)
    cur = newhead

    while left and right:
        if left.val<=right.val:
            cur.next = left
            left = left.next
            cur = cur.next
        else:
            cur.next = right
            right = right.next
            cur = cur.next
    
    if left:
        cur.next = left
    
    if right:
        cur.next = right
    
    return newhead.next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        for i in lists:
            merged = merge(merged,i)
        
        return merged

        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(head1: List[Optional[ListNode]],head2: List[Optional[ListNode]]) -> Optional[ListNode]:
    left, right = head1, head2
    newhead = ListNode(-10001)
    cur = newhead

    while left and right:
        if left.val<=right.val:
            temp = left.next
            left.next = cur.next
            cur.next = left
            left = temp
        else:
            temp = right.next
            right.next = cur.next
            cur.next = right
            right = temp
        cur = cur.next
    
    if left:
        cur.next = left
    
    if right:
        cur.next = right
    
    return newhead


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newhead = ListNode(-10001)
        cur = newhead
        for i in lists:
            cur = merge(cur,i)
        
        return newhead.next

        
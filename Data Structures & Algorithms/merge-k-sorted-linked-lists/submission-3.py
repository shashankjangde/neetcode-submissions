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
        merged_list = []
        while len(lists)>1:
            for i in range(0,len(lists),2):
                left = lists[i]
                right = lists[i+1] if i+1<len(lists) else None
                merged_list.append(merge(left, right))
            
            lists = merged_list[::]
            merged_list = []
        
        return lists[0] if len(lists) else None
            


        
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d1 = {None:None}
        cur = head
        new_cur = None
        while cur: 
            new = Node(cur.val)
            d1[cur] = new
            cur = cur.next

        cur = head
        nh = d1[cur]
        while cur: 
            nc = d1[cur]
            nc.next = d1[cur.next]
            nc.random = d1[cur.random]
            cur = cur.next
        return nh
        
        


    
        



        
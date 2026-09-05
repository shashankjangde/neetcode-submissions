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
            d1[cur.val] = new
            cur = cur.next

        cur = head
        nh = d1[cur.val]
        while cur: 
            nc = d1[cur.val]
            if cur.next != None:
                nc.next = d1[cur.next.val]
            else:
                nc.next = None
            if cur.random != None:
                nc.random = d1[cur.random.val]
            else:
                nc.random = None
            cur = cur.next
        return nh
        
        


    
        



        
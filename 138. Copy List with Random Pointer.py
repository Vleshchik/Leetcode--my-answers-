"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur: # copy nodes
            node = Node(cur.val, cur.next)
            cur.next = node
            cur = node.next

        cur = head
        while cur: # copy random pointers
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        ans = head.next
        cur = head
        while cur: # cut into 2 lists
            nxt = cur.next
            if nxt:
                cur.next = nxt.next
            cur = nxt
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head.next is None or left == right:
            return head
        rev_head = ListNode(0, head)
        pre = rev_head
        for _ in range(left - 1):
            pre = pre.next
        p, q = pre, pre.next
        cur = q
        # +1, so when for loop done, 'cur' is at right's next node
        for _ in range(right - left + 1):
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        p.next = pre
        # p,q did not change by the for loop, but now pre at right(or called m) node, cur at right+1 node
        q.next = cur
        return rev_head.next
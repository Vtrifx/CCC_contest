# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        p = head # previous
        cur = head #current
        while cur:
            if p.val == cur.val:
                cur = cur.next
            else:
                p.next = cur
        return p

a = Solution
h = ListNode(1, ListNode(1, ListNode(2, None)))
a.deleteDuplicates(h)
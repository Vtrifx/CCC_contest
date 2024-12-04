
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        n = head

        while cur:
            n = n.next
            n.head = cur
            cur = cur.next
        return n


if __name__ == "__main__":
    print(Solution().reverseList([1,2,3,4,5]))
class Solution:
    def middleNode(self, head: option[ListNode]) -> Optional[ListNode]:
        slow,fast = head, head
        while fast and fast.next:
            slow.next
            fast.next.next
        return slow
if __name__ == "__main__":
    print(Solution().middleNode([1,2,3,4,5]))
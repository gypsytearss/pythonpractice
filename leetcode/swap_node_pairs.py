class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other) -> bool:
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False


class Solution:
    """
    https://leetcode.com/problems/swap-nodes-in-pairs/
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = None
        prev = None
        current = head
        while current and current.next:
            tmp = current.next.next
            current.next.next = current
            if not new_head:
                new_head = current.next
            if prev:
                prev.next = current.next
            prev = current
            current.next = tmp
            current = tmp
        return new_head or head
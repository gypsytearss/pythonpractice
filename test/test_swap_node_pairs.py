import pytest
from leetcode.swap_node_pairs import ListNode
from leetcode.swap_node_pairs import Solution

def test_basic():
    test_head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
    expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3, None))))

    sol = Solution()
    assert sol.swapPairs(test_head) == expected
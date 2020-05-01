import pytest
from leetcode.swap_node_pairs import ListNode
from leetcode.swap_node_pairs import Solution

@pytest.fixture
def list_node():
    return ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

def test_basic(list_node):
    expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3, None))))

    sol = Solution()
    assert sol.swapPairs(list_node) == expected
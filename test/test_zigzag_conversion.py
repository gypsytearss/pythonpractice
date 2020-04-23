import pytest
from leetcode.zigzag_conversion import Solution

def test_zigzag_1():
    test_string = "abcdefghijkl"
    num_rows = 3
    expected = "aeibdfhjlcgk"

    sol = Solution()
    assert sol.convert(test_string, num_rows) == expected


def test_zigzag_2():
    test_string = "ab"
    num_rows = 1
    expected = "ab"

    sol = Solution()
    assert sol.convert(test_string, num_rows) == expected
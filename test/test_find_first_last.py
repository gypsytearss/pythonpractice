import pytest
from leetcode.find_first_last_sorted import Solution

def test_find_left():
    test_nums = [0,1,2]
    target = 1

    sol = Solution()
    assert sol.searchLeft(test_nums, target, 0) == 1

def test_find_first_last_1():
    test_nums = [2,3,4,6,6,7,7,8]
    target = 6
    expected = [3,4]

    sol = Solution()
    assert sol.searchRange(test_nums, target) == expected

    bad_target = 5
    bad_expected = [-1, -1]
    assert sol.searchRange(test_nums, bad_target) == bad_expected
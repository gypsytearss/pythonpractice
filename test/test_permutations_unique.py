import pytest
from leetcode.permutations_unique import Solution

def test_simple_permutations():
    test_nums = [0,1,2]

    sol = Solution()
    res = sol.permuteUnique(test_nums)
    assert [0,1,2] in res
    assert [1,0,2] in res
    assert [1,2,0] in res
    assert [0,2,1] in res
    assert [2,0,1] in res
    assert [2,1,0] in res
    assert len(res) == 6

def test_unique_permutations():
    test_nums = [1,1,2]

    sol = Solution()
    res = sol.permuteUnique(test_nums)
    assert [1,1,2] in res
    assert [1,2,1] in res
    assert [2,1,1] in res
    assert len(res) == 3

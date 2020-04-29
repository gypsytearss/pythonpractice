from typing import List

class Solution:
    """
    https://leetcode.com/problems/permutations-ii/
    """
    def interleave(self, num: int, perms: List[List[int]]) -> List[List[int]]:
        if not perms:
            return [[num]]
        else:
            return [p[0:i] + [num] + p[i:] for p in perms for i in range(0, len(p) + 1)]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            res = self.interleave(nums[0], self.permuteUnique(nums[1:]))
            return [list(map(int, u.split("_"))) for u in set(["_".join(map(str, p)) for p in res])]